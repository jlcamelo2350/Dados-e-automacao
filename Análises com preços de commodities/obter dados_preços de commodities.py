import yfinance as yf
import os
import pandas as pd
import datetime as dt

# Lista de produtos que buscarei os preços
tickers = [
    "CL=F",  # Crude Oil
    "BZ=F",  # Brent Crude Oil
    "NG=F",  # Natural Gas
    "GC=F",  # Gold
    "SI=F",  # Silver
    "HG=F",  # Copper
    "PA=F",  # Palladium
    "PL=F",  # Platinum
    "ZC=F",  # Corn
    "ZW=F",  # Wheat
    "ZS=F",  # Soybeans
    "KC=F",  # Coffee
    "CT=F",  # Cotton
    "SB=F",  # Sugar
    "OJ=F",  # Orange Juice
    "LBS=F",  # Lumber
    "LE=F",  # Live Cattle
    "GF=F",  # Feeder Cattle
    "HE=F",  # Lean Hogs
    "CC=F",  # Cocoa
    "SM=F",  # Soybean Meal
    "BO=F",  # Soybean Oil
    "RR=F",  # Rough Rice
    "HO=F",  # Heating Oil
    "RB=F",  # RBOB Gasoline
    "MGC=F",  # Micro Gold
    "SIL=F",  # Micro Silver
    "ZT=F",  # 2-Year T-Note
    "ZF=F",  # 5-Year T-Note
    "ZN=F",  # 10-Year T-Note
    "ZB=F",  # 30-Year T-Bond
    "ES=F",  # S&P 500 Futures
    "YM=F",  # Dow Jones Futures
    "NQ=F",  # Nasdaq Futures
    "RTY=F",  # Russell 2000 Futures
    "ZO=F",  # Oats
    "KE=F",  # KC HRW Wheat
    "ZR=F",  # Rough Rice
    "ZM=F",  # Soybean Meal
    "ZL=F",  # Soybean Oil
    "GF=F",  # Feeder Cattle
    "HE=F",  # Lean Hogs
    "LE=F",  # Live Cattle
    "CC=F",  # Cocoa
    "KC=F",  # Coffee
    "CT=F",  # Cotton
    "LBS=F",  # Lumber
    "OJ=F",  # Orange Juice
    "SB=F",  # Sugar
]


df = pd.DataFrame()

start = dt.datetime(2000, 1, 2)
end = dt.datetime(2024, 4, 1)

 # Baixar os dados de fechamento para cada commodity e armazenar no DataFrame df
for ticker in tickers:
    try:
        data = yf.download(ticker, start=start, end=end)['Close']
        # Renomear a coluna do DataFrame para incluir o ticker
        data = data.rename(ticker)
        df = pd.concat([df, data], axis=1)
    except Exception as e:
        print(f"Erro ao baixar dados para {ticker}: {e}")

# Resetar o índice para incluir a coluna de datas no DataFrame
df.reset_index(inplace=True)

# Mostrar as primeiras linhas do DataFrame
print(df.head())

caminho = os.path.join(os.path.expanduser('~'), 'Downloads')
df.to_excel(os.path.join(caminho, 'commodities.xlsx'), index=False)
