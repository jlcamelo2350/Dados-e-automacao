#Importo as bibliotecas que utilizarei
import yfinance as yf
import os
import pandas as pd
import datetime as dt

# crio um dataframe onde armazenarei os dados
df = pd.DataFrame()

#data dos dados, que vai entre janeiro de 2000 a maio de 2024
start = dt.datetime(2000, 1, 2)
end = dt.datetime(2024, 4, 1)

# Defino o ticker para o petróleo bruto WTI
ticker = "CL=F"

#Baixo os dados dos preços do petróleo
data = yf.download(ticker, start=start, end=end)['Close']

# Renomear a coluna do DataFrame para incluir o ticker.
df[ticker.split('.')[0]] = data

# Resetar o índice para incluir a coluna de datas no DataFrame
df.reset_index(inplace=True)

# Mostrar as primeiras linhas do DataFrame
print(df.head())

#Salvo os dados em uma planilha excel que será salvo na pasta de downloads com o nome petróleo.xlsx
caminho = os.path.join(os.path.expanduser('~'), 'Downloads')
df.to_excel(os.path.join(caminho, 'petróleo.xlsx'), index=False)
