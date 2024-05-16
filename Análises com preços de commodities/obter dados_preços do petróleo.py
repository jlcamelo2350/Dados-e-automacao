import yfinance as yf
import os
import pandas as pd
import datetime as dt

# Define o ticker para o petróleo bruto WTI
ticker = "CL=F"

df = pd.DataFrame()

start = dt.datetime(2000, 1, 2)
end = dt.datetime(2024, 4, 1)

data = yf.download(ticker, start=start, end=end)['Close']

# Renomear a coluna do DataFrame para incluir o ticker.
df[ticker.split('.')[0]] = data

# Resetar o índice para incluir a coluna de datas no DataFrame
df.reset_index(inplace=True)

# Mostrar as primeiras linhas do DataFrame
print(df.head())

caminho = os.path.join(os.path.expanduser('~'), 'Downloads')
df.to_excel(os.path.join(caminho, 'petróleo.xlsx'), index=False)
