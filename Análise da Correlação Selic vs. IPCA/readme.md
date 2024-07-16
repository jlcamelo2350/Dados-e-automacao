# Análise da Relação entre Taxa Selic e Inflação no Brasil 📊💹

Este projeto realiza uma análise detalhada da relação entre a taxa Selic e a inflação medida pelo IPCA no Brasil, abordando diferentes períodos e utilizando modelos estatísticos para entender a dinâmica entre essas variáveis.

## Objetivos 🎯

- Investigar a correlação entre a taxa Selic e a variação do IPCA em diferentes períodos.
- Avaliar o impacto da política monetária na inflação ao longo do tempo.
- Comparar os efeitos de transmissão da política monetária nos EUA com o Brasil.

## Insight:
- Deve-se estudar mais os dados e combinar isso com a teoria econômica, de maneira a se buscar quais os mecanismos de transmissão da política monetária que estão deficientes no Brasil e como consertar isso -- se se quiser obter o máximo de resultados da política monetária aqui.

## Estrutura do Projeto 📑

### 1. Coleta de Dados 📊

Os dados são extraídos de diferentes fontes, incluindo:

- **Taxa Selic**: Obtido diretamente via Python pela biblioteca `python-bcv`
- **IPCA**: Base de dados do IBGE + limpeza e organização dos dados via excel e python.
- **Inflação nos EUA**: Dados coletados de fontes públicas (st.louis FED) e organizados por mim no Excel

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
- A economia brasileira tem uma certa deficiência de absorção da política monetária em comparação com a economia estadunidense.

### 4. Modelagem ARIMA 📊

Um modelo ARIMA foi aplicado para avaliar a relação entre a Selic e a inflação. Os resultados indicaram que a Selic não explica adequadamente a variação do IPCA, embora exista uma relação observável, no caso brasileiro.

### 5. Comparação Internacional 🌍

Os dados da inflação e taxa de juros dos EUA foram analisados para comparar a dinâmica inflacionária lá e aqui. Sobretudo, estudou-se a capacidade de absorção dos efeitos da política monetária nessa economia.

## Resultados Gráficos 📊📈

Gráficos foram gerados para visualizar:
Todos os resultados obtidos são representados também por meios visuais de forma a melhorar a análise e facilitar o entendimento 

-  correlação entre Selic e IPCA ao longo dos meses.
-  evolução da inflação no Brasil e nos EUA.
  
## Conclusões 🎓

- A política monetária no Brasil apresenta desafios significativos na transmissão de seus efeitos à economia.
- Deve-se investigar as causas dessa deficiência de transmissão da política monetária na economima brasileira e resolver o problema, de modo que o país consiga após isso usufruir dos efeitos da política monetária em sua plenitude. Isso implicará em melhora do funcionamento da economia nacional.
- A economia estadunidense é um bom exemplo de pleno funcionamento e capacidade de transmissão da política monetária.

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

Para dúvidas ou sugestões, entre em contato: jlcam3250@gmail.com

---

Agradecemos por acompanhar este projeto! Esperamos que os insights aqui apresentados contribuam para uma melhor compreensão da dinâmica econômica brasileira.

---

Este projeto foi criado para inspirar e facilitar a análise macroeconômica. Espero que você encontre valor neste trabalho e utilize-o para aprimorar suas próprias pesquisas e projetos. **Paz** 🖖 🌟

---
