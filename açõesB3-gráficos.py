#Código em python que baixa os dados de várias ações no período entre 2022 e 2024
#Depois, desenha-se o gráfico dessas ações.

#Importo as bibliotecas para uso no python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import gdown
import os

# URL do arquivo Excel no Google Drive (link de download direto)
url = 'https://docs.google.com/spreadsheets/d/1fG-I1Sn3sv_vIFZAGl2C54zLvw-Xqmit/export?format=xlsx'

# faço o download do arquivo
downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
caminho = os.path.join(downloads_dir, 'portfólio_RV.xlsx')

# Faz o download do arquivo
gdown.download(url, caminho, quiet=False)

# Carregar os dados do arquivo Excel
dados = pd.read_excel(caminho, index_col=0, parse_dates=True)

empresas = dados.columns

# Plotar um gráfico de linha para cada coluna da planilha
for empresa in empresas:
    plt.figure(figsize=(12, 6))

    # Desenho um gráfico de linhas para cada empresa
    plt.plot(dados.index, dados[empresa], label=empresa, color=np.random.choice(['red', 'blue', 'green']))
    
    # Desenho uma linha de tendência para empresa
    coef = np.polyfit(range(len(dados)), dados[empresa], 1)
    tendencia = np.polyval(coef, range(len(dados)))
    plt.plot(dados.index, tendencia, linestyle='--', color='black')

    plt.xlabel('Data')
    plt.ylabel('Preço da Ação')
    plt.title(f'Preço da Ação {empresa} ao Longo do Tempo')
    plt.legend()
    plt.grid(True)
    plt.show()
