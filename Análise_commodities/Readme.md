# 📈 Previsão de Preços de Commodities

## 📝 Descrição do Projeto

Este projeto visa a modelagem preditiva dos preços de commodities exportadas pelo Brasil, utilizando dados históricos e técnicas de aprendizado de máquina. O objetivo é gerar previsões confiáveis para os preços de commodities como açúcar, soja, milho, trigo, café, ouro, petróleo, madeira, cobre e gado vivo.

## 🛠️ Tecnologias Utilizadas

- **Linguagem de Programação:** Python
- **Bibliotecas:** 
  - `pandas` para manipulação de dados
  - `numpy` para operações numéricas
  - `matplotlib` e `seaborn` para visualização de dados
  - `scikit-learn` para modelagem preditiva
  - `yfinance` para coleta de dados financeiros

## 📊 Metodologia
O projeto consiste em várias etapas:

- **Coleta de Dados:** Os dados históricos de preços das commodities são coletados utilizando a biblioteca yfinance.
- **Análise Exploratória:** Análise da volatilidade e estatísticas descritivas dos preços.
- **Modelagem Preditiva:** Implementação de diferentes modelos de regressão, para escolher o que melhor se adequa à modelagem (Linear Regression, Ridge, Lasso, ElasticNet, Random Forest).
- **Visualização:** Geração de gráficos comparativos entre os preços reais e previstos, bem como a comparação dos scores R² de cada modelo.
- **Previsões Futuras:** Geração de previsões para os próximos dias com base nos modelos treinados.

## 📈 Resultados
- Modelagem preditiva dos preços para as próximas 100 cotações.
