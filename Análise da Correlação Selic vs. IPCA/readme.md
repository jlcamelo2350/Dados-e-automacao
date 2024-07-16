# Análise da Relação entre Taxa Selic e Inflação no Brasil 📊💹

Este projeto realiza uma análise detalhada da relação entre a taxa Selic e a inflação medida pelo IPCA no Brasil, abordando diferentes períodos e utilizando modelos estatísticos para entender a dinâmica entre essas variáveis.

## Objetivos 🎯

- Investigar a correlação entre a taxa Selic e a variação do IPCA em diferentes períodos.
- Avaliar o impacto da política monetária na inflação ao longo do tempo.
- Comparar os resultados da inflação brasileira com os dados dos Estados Unidos.

## Estrutura do Projeto 📑

### 1. Coleta de Dados 📊

Os dados são extraídos de diferentes fontes, incluindo:

- **Taxa Selic**: Base de dados própria ou pública.
- **IPCA**: Dados históricos obtidos de planilhas do Google.
- **Inflação nos EUA**: Dados coletados de fontes públicas.

### 2. Análise de Dados 📈

Os dados são filtrados em dois períodos:

- **2000 a 2024**
- **2000 a 2010**
- **2010 a 2024**

Em cada período, são calculadas as correlações entre a variação da Selic e a variação do IPCA com diferentes lags.

### 3. Resultados 📉

Os resultados das correlações foram visualizados através de gráficos, evidenciando que:

- O impacto da Selic na inflação tende a se manifestar apenas após vários meses.
- A correlação é mais forte em períodos posteriores, indicando uma maior eficácia da política monetária no médio prazo.

### 4. Modelagem ARIMA 📊

Um modelo ARIMA foi aplicado para avaliar a relação entre a Selic e a inflação. Os resultados indicaram que a Selic não explica adequadamente a variação do IPCA, embora exista uma relação observável.

### 5. Comparação Internacional 🌍

Os dados da inflação e taxa de juros dos EUA foram analisados para comparar a dinâmica inflacionária entre Brasil e EUA.

## Resultados Gráficos 📊📈

Gráficos foram gerados para visualizar:

- A correlação entre Selic e IPCA ao longo dos meses.
- A evolução da inflação no Brasil e nos EUA.

## Conclusões 🎓

- A política monetária no Brasil apresenta desafios significativos na transmissão de seus efeitos à economia.
- O modelo de Tripé Macroeconômico, embora mal implementado, ainda resulta em uma tendência de queda da inflação ao longo do tempo.

## Tecnologias Utilizadas 🛠️

- **Python**: Para análise de dados e modelagem estatística.
- **Pandas**: Manipulação de dados.
- **Statsmodels**: Modelagem ARIMA.
- **Matplotlib e Seaborn**: Visualização de dados.

## Como Executar o Projeto ▶️

1. Clone o repositório.
2. Instale as dependências necessárias usando `pip install -r requirements.txt`.
3. Execute o script principal para gerar as análises e visualizações.

## Contato 📧

Para dúvidas ou sugestões, entre em contato: [seu_email@dominio.com](mailto:seu_email@dominio.com).

---

Agradecemos por acompanhar este projeto! Esperamos que os insights aqui apresentados contribuam para uma melhor compreensão da dinâmica econômica brasileira.


