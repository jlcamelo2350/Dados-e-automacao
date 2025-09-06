"""
=========================================================
 Customer Classification Pipeline (versão anonimizada)
=========================================================

Este script conecta em um banco de dados SQL Server, unifica dados
de vendas de diferentes fontes (loja física e canal alternativo),
calcula métricas por cliente (últimos 12 meses e 13–24 meses anteriores)
e classifica os clientes em diferentes grupos, como:

- 01 - FANS
- 02 - PREMIUM
- 03 - SUPER VIP
- 04 - VIP
- 05 - POTENTIAL
- 06 - GOOD
- 07 - OK
- 10 - NEW BUYERS
- 11 - ONE TIME BUYERS
- 20 - INACTIVE HP
- 21 - RECENTLY INACTIVE
- 22 - LOST
- 23 - NEVER BOUGHT

O resultado é exportado em formato CSV com histórico de classificações
para múltiplos anos.

⚠️ Todos os nomes de tabelas e colunas foram substituídos por genéricos,
mantendo apenas a lógica de negócio. Use os nomes reais no ambiente de
produção conforme necessário.
"""


import os
import logging
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from contextlib import closing
import warnings

import numpy as np
import pandas as pd
import pyodbc
from dataclasses import dataclass

warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('classificacao_clientes.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# -----------------------------
# Configuração de Banco de Dados
# -----------------------------
@dataclass
class DatabaseConfig:
    server: str   = 'my_server'
    username: str = 'my_user'
    password: str = 'my_password'
    database: str = 'my_database'

# -----------------------------
# Thresholds de classificação
# -----------------------------
@dataclass
class ClassificationThresholds:
    fas_freq: int = 4
    fas_valor: float = 40000
    premium_freq: int = 4
    premium_valor_min: float = 15000
    premium_valor_max: float = 40000
    super_vip_valor: float = 15000
    super_vip_valor_alt_min: float = 8049
    super_vip_valor_alt_max: float = 15000
    vip_valor_min: float = 4044
    vip_valor_max: float = 8048
    potencial_valor_min: float = 2190
    potencial_valor_max: float = 4044
    bom_valor_min: float = 963
    bom_valor_max: float = 2190
    ok_valor_max: float = 962
    new_buyers_months: int = 6
    one_time_buyers_months: int = 12
    inativos_hp_threshold: float = 8000

class CustomerClassifierOptimized:
    def __init__(self, config: DatabaseConfig, thresholds: ClassificationThresholds, export_dir: str = None):
        self.config = config
        self.thresholds = thresholds
        self.export_dir = export_dir or os.getcwd()
        self.conn_str = (
            f"DRIVER={{SQL Server}};SERVER={config.server};"
            f"DATABASE={config.database};UID={config.username};PWD={config.password}"
        )

    def get_connection(self) -> pyodbc.Connection:
        return pyodbc.connect(self.conn_str)

    # --------------------- carregar dados de clientes ---------------------
    def load_clients_data(self) -> pd.DataFrame:
        query = """
        SELECT
            LTRIM(RTRIM(UPPER(CUSTOMER_ID))) AS CUSTOMER_ID,
            CUSTOMER_NAME
        FROM CUSTOMERS_TABLE
        WHERE CUSTOMER_ID IS NOT NULL AND LTRIM(RTRIM(CUSTOMER_ID)) <> ''
        """
        with closing(self.get_connection()) as conn:
            df = pd.read_sql(query, conn)

        df['CUSTOMER_ID'] = (
            df['CUSTOMER_ID']
              .astype('string')
              .str.strip()
              .str.replace(r'\.0$', '', regex=True)
        )

        if 'CUSTOMER_NAME' in df.columns:
            df['CUSTOMER_NAME'] = df['CUSTOMER_NAME'].astype('string').str.strip()

        df = df.drop_duplicates(subset=['CUSTOMER_ID'])
        return df
    # ---------------------------------------------------------------------

    def load_sales_data_optimized(self) -> pd.DataFrame:
        query = """
        WITH sales_unified AS (
            SELECT LTRIM(RTRIM(UPPER(TICKET))) AS TICKET, SALE_DATE,
                   LTRIM(RTRIM(UPPER(CUSTOMER_ID))) AS CUSTOMER_ID,
                   LTRIM(RTRIM(UPPER(STORE_ID))) AS STORE_ID,
                   LTRIM(RTRIM(UPPER(SELLER))) AS SELLER,
                   LTRIM(RTRIM(UPPER(SALE_OP))) AS SALE_OP,
                   CAST(VALUE_PAID AS FLOAT) AS VALUE_PAID,
                   CAST(QTY AS INT) AS QTY,
                   'MAIN' AS SOURCE
            FROM SALES_MAIN_TABLE
            WHERE SALE_DATE IS NOT NULL AND CUSTOMER_ID <> '' AND VALUE_PAID > 0
            UNION ALL
            SELECT LTRIM(RTRIM(UPPER(TICKET))) AS TICKET, SALE_DATE,
                   NULL AS CUSTOMER_ID,
                   LTRIM(RTRIM(UPPER(STORE_ID))) AS STORE_ID,
                   LTRIM(RTRIM(UPPER(SELLER))) AS SELLER,
                   NULL AS SALE_OP,
                   CAST(VALUE_UNIT AS FLOAT) AS VALUE_PAID,
                   CAST(QTY AS INT) AS QTY,
                   'ALT' AS SOURCE
            FROM SALES_ALT_TABLE
            WHERE SALE_DATE IS NOT NULL AND VALUE_UNIT > 0
        )
        SELECT *
        FROM sales_unified
        WHERE SALE_DATE >= DATEADD(year, -6, GETDATE())
        ORDER BY SALE_DATE DESC
        """
        with closing(self.get_connection()) as conn:
            logger.info("Executando query de vendas em chunks...")
            chunks = [chunk for chunk in pd.read_sql(query, conn, chunksize=100_000)]
            df = pd.concat(chunks, ignore_index=True)

        if 'CUSTOMER_ID' in df.columns:
            df['CUSTOMER_ID'] = (
                df['CUSTOMER_ID']
                  .astype('string')
                  .str.strip()
                  .str.replace(r'\.0$', '', regex=True)
            )

        df['VALUE_PAID'] = pd.to_numeric(df['VALUE_PAID'], errors='coerce')
        df['QTY'] = pd.to_numeric(df['QTY'], errors='coerce').fillna(0).astype(int)
        df['SALE_DATE'] = pd.to_datetime(df['SALE_DATE'], errors='coerce')

        df = df[df['SALE_DATE'].notna() & df['CUSTOMER_ID'].notna() & (df['CUSTOMER_ID'] != '')]

        logger.info(f"Carregados {len(df):,} registros de vendas após limpeza")
        return df

    def calculate_metrics_vectorized(self, df_sales: pd.DataFrame, reference_date: datetime) -> pd.DataFrame:
        df = df_sales[df_sales['SALE_DATE'] <= reference_date].copy()
        if df.empty:
            return pd.DataFrame()

        limit_12m = reference_date - relativedelta(months=12)
        limit_24m = reference_date - relativedelta(months=24)

        df['is_12m'] = df['SALE_DATE'] >= limit_12m
        df['is_13_24m'] = (df['SALE_DATE'] >= limit_24m) & (df['SALE_DATE'] < limit_12m)

        base = df.groupby('CUSTOMER_ID').agg(
            valor_total=('VALUE_PAID', 'sum'),
            primeira_compra=('SALE_DATE', 'min'),
            ultima_compra=('SALE_DATE', 'max'),
            tickets_total=('TICKET', 'nunique')
        ).reset_index()

        m12 = df[df['is_12m']].groupby('CUSTOMER_ID').agg(
            valor_12m=('VALUE_PAID', 'sum'),
            freq_12m=('TICKET', 'nunique')
        ).reset_index()

        m13_24 = df[df['is_13_24m']].groupby('CUSTOMER_ID').agg(
            valor_13a24m=('VALUE_PAID', 'sum')
        ).reset_index()

        metrics = base.merge(m12, on='CUSTOMER_ID', how='left').fillna({'valor_12m': 0, 'freq_12m': 0})
        metrics = metrics.merge(m13_24, on='CUSTOMER_ID', how='left').fillna({'valor_13a24m': 0})

        delta_months = ((reference_date.year - metrics['primeira_compra'].dt.year) * 12 +
                        (reference_date.month - metrics['primeira_compra'].dt.month))
        metrics['meses_desde_primeira'] = delta_months.fillna(0).astype(int)
        metrics['dias_desde_ultima'] = (reference_date - metrics['ultima_compra']).dt.days

        return metrics

    def classify_customers_vectorized(self, df: pd.DataFrame, reference_date: datetime) -> pd.DataFrame:
        t = self.thresholds
        df = df.copy()
        df['classificacao'] = "99 - UNCLASSIFIED"

        period_start = reference_date - relativedelta(months=12)
        mask_ativo = df['valor_12m'] > 0
        primeira = df['primeira_compra']

        df.loc[primeira.isna(), 'classificacao'] = "23 - NEVER BOUGHT"
        df.loc[(df['valor_12m'] == 0) & (df['valor_13a24m'] == 0), 'classificacao'] = "22 - LOST"
        df.loc[(df['valor_12m'] == 0) & (df['valor_13a24m'] > t.inativos_hp_threshold), 'classificacao'] = "20 - INACTIVE HP"
        df.loc[(df['valor_12m'] == 0) & (df['valor_13a24m'] > 0) & (df['valor_13a24m'] <= t.inativos_hp_threshold), 'classificacao'] = "21 - RECENTLY INACTIVE"

        first_in_period = (primeira >= period_start) & (primeira <= reference_date)

        mask_new = (
            mask_ativo
            & first_in_period
            & (df['freq_12m'] == 1)
            & (df['meses_desde_primeira'] <= t.new_buyers_months)
        )
        df.loc[mask_new, 'classificacao'] = "10 - NEW BUYERS"

        mask_one = (
            mask_ativo
            & first_in_period
            & (df['freq_12m'] == 1)
            & (df['meses_desde_primeira'] > t.new_buyers_months)
            & (df['meses_desde_primeira'] <= t.one_time_buyers_months)
        )
        df.loc[mask_one & (df['classificacao'] == "99 - UNCLASSIFIED"), 'classificacao'] = "11 - ONE TIME BUYERS"

        mask_est = mask_ativo & ((~first_in_period) | (df['freq_12m'] >= 2) | (df['meses_desde_primeira'] > t.one_time_buyers_months))

        df.loc[mask_est & (df['freq_12m'] >= t.fas_freq) & (df['valor_12m'] >= t.fas_valor), 'classificacao'] = "01 - FANS"

        df.loc[
            mask_est
            & (df['freq_12m'] >= t.premium_freq)
            & (df['valor_12m'].between(t.premium_valor_min, t.premium_valor_max, inclusive='left'))
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "02 - PREMIUM"

        df.loc[
            mask_est
            & (
                ((df['freq_12m'] < t.premium_freq) & (df['valor_12m'] >= t.super_vip_valor))
                | (df['valor_12m'].between(t.super_vip_valor_alt_min, t.super_vip_valor_alt_max, inclusive='left'))
            )
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "03 - SUPER VIP"

        df.loc[
            mask_est
            & (df['valor_12m'].between(t.vip_valor_min, t.vip_valor_max))
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "04 - VIP"

        df.loc[
            mask_est
            & (df['valor_12m'].between(t.potencial_valor_min, t.potencial_valor_max, inclusive='left'))
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "05 - POTENTIAL"

        df.loc[
            mask_est
            & (df['valor_12m'].between(t.bom_valor_min, t.bom_valor_max, inclusive='left'))
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "06 - GOOD"

        df.loc[
            mask_est
            & (df['valor_12m'] > 0)
            & (df['valor_12m'] <= t.ok_valor_max)
            & (df['classificacao'] == "99 - UNCLASSIFIED"),
            'classificacao'
        ] = "07 - OK"

        return df

    def generate_historical_classification(self, years: list) -> pd.DataFrame:
        df_sales = self.load_sales_data_optimized()
        reference_date = datetime.today() - timedelta(days=1)

        result_frames = []
        for year in years:
            offset = max(years) - year
            year_ref = reference_date - relativedelta(years=offset)

            metrics = self.calculate_metrics_vectorized(df_sales, year_ref)
            if metrics.empty:
                continue

            classified = self.classify_customers_vectorized(metrics, year_ref)
            classified = classified[['CUSTOMER_ID', 'classificacao']].rename(columns={'classificacao': f'classificacao_{year}'})
            result_frames.append(classified)

        if not result_frames:
            return pd.DataFrame()

        df_final = result_frames[0]
        for df in result_frames[1:]:
            df_final = df_final.merge(df, on='CUSTOMER_ID', how='outer')

        # --------------------- merge com tabela de clientes ---------------------
        df_clientes = self.load_clients_data()
        df_final = df_final.merge(df_clientes, on='CUSTOMER_ID', how='left')

        cols = ['CUSTOMER_ID', 'CUSTOMER_NAME'] + [c for c in df_final.columns if c not in ['CUSTOMER_ID', 'CUSTOMER_NAME']]
        df_final = df_final[cols]
        # -------------------------------------------------------------------

        return df_final

    def export_results(self, df: pd.DataFrame, filename_prefix: str = "CUSTOMERS_CLASSIFICATION_HISTORY") -> str:
        if df.empty:
            raise ValueError("DataFrame vazio")
        filename = f"{filename_prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        filepath = os.path.join(self.export_dir, filename)
        df.to_csv(filepath, index=False, encoding='utf-8-sig')
        logger.info(f"Arquivo salvo em: {filepath}")
        return filepath

# Execução
if __name__ == '__main__':
    config     = DatabaseConfig()
    thresholds = ClassificationThresholds()
    classifier = CustomerClassifierOptimized(config, thresholds)
    anos       = list(range(datetime.today().year - 4, datetime.today().year + 1))

    df_historico = classifier.generate_historical_classification(anos)
    if not df_historico.empty:
        path = classifier.export_results(df_historico)
        print(f"✅ Exportado em: {path}")
    else:
        print("Nenhum dado para exportar.")

