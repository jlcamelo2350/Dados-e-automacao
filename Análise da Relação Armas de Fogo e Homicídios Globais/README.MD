# 🔫 Armas de Fogo e Violência: Uma Análise Multifacetada da Relação entre Posse de Armas e Homicídios no Contexto Global

Este projeto explora a relação entre a posse de armas de fogo civis e a violência, especialmente as mortes violentas, em diferentes países ao redor do mundo. Utilizo uma abordagem baseada em aprendizado de máquina para agrupar países em clusters, a fim de identificar padrões e comportamentos semelhantes em relação à violência armada.

<img src="https://github.com/jlcamelo2350/Dados-e-automacao/blob/main/An%C3%A1lise%20da%20Rela%C3%A7%C3%A3o%20Armas%20de%20Fogo%20e%20Homic%C3%ADdios%20Globais/gr%C3%A1ficos/gr%C3%A1fico%20-%20all%20clusters.png" alt="Relação entre população, armas de fogo e mortes violentas (All Clusters)" width="800" height="500">

## 📋 Descrição do Projeto

O objetivo deste projeto é analisar como a posse de armas civis pode estar relacionada com os níveis de violência em diferentes nações. Para isso, utilizamos dados sobre **população**, **mortes violentas por 100k habitantes** e **armas de fogo civis por 100 habitantes**. O estudo busca encontrar padrões globais e identificar países que compartilham semelhanças neste aspecto crítico da segurança pública.

### 🔍 Metodologia

A análise foi conduzida em várias etapas:

1. **Pré-processamento dos Dados**: 
   - Os dados foram normalizados e padronizados para garantir que os valores estivessem na mesma escala.
   
2. **Análise Exploratória**: 
   - Uma análise inicial dos dados foi realizada para obter insights sobre as distribuições de variáveis como população e número de armas civis.
   
3. **Clustering (K-Means)**:
   - Aplicamos a técnica de clustering K-Means para agrupar os países em grupos (clusters) baseados em suas características.
   - A escolha do número ideal de clusters foi feita com base na análise do método do cotovelo, resultando em um modelo com **k = 5**.

4. **Visualizações**:
   - Utilizamos gráficos de dispersão 2D e gráficos de bolhas para visualizar as relações entre as variáveis e os países dentro de cada cluster.

### 🔑 Principais Ferramentas e Tecnologias Utilizadas

- **Python**: Linguagem principal usada para a análise e visualização de dados.
- **Bibliotecas**:
  - `pandas`: Manipulação e análise dos dados.
  - `numpy`: Operações numéricas e estatísticas.
  - `matplotlib` e `seaborn`: Visualizações gráficas.
  - `plotly.express`: Visualizações interativas.
  - `scikit-learn`: Algoritmos de machine learning para clustering.

### 🔢 Detalhamento dos Clusters

A análise resultou na criação de **6 clusters**, cada um agrupando países com características similares em termos de posse de armas e violência. Abaixo, os principais insights de cada cluster:

#### Cluster 4: Alta Violência e Alta Posse de Armas
- **Países**: Brasil, Colômbia, El Salvador, Guatemala, Honduras, Venezuela.
- **Características**:
  - Todos são países latinos
  - Altos níveis de violência armada e posse não elevada (apenas a Venezuela tem um pouco mais) de armas civis.
  - Estes países enfrentam crises de segurança pública profundas.

Gráfico de bolhas mostrando a relação entre população, armas de fogo civis e mortes violentas (Cluster 4):
<img src="https://github.com/jlcamelo2350/Dados-e-automacao/blob/main/An%C3%A1lise%20da%20Rela%C3%A7%C3%A3o%20Armas%20de%20Fogo%20e%20Homic%C3%ADdios%20Globais/gr%C3%A1ficos/Rela%C3%A7%C3%A3o%20entre%20popula%C3%A7%C3%A3o%2C%20armas%20de%20fogo%20e%20mortes%20violentas%20(Cluster%204).png" alt="Relação entre população, armas de fogo e mortes violentas (Cluster 4)" width="500" height="300">


#### Cluster 1: População Moderada e Baixa Violência
- **Países**: Exemplo de países.
- **Características**:
  - Países de diversos continentes.
  - Níveis moderados de posse de armas civis, porém, menores taxas de violência, em relação à cluster 4.

Gráfico de bolhas representando os países deste cluster 1:

<img src="https://github.com/jlcamelo2350/Dados-e-automacao/blob/main/An%C3%A1lise%20da%20Rela%C3%A7%C3%A3o%20Armas%20de%20Fogo%20e%20Homic%C3%ADdios%20Globais/gr%C3%A1ficos/Rela%C3%A7%C3%A3o%20entre%20popula%C3%A7%C3%A3o%2C%20armas%20de%20fogo%20e%20mortes%20violentas%20(Cluster%201).png" alt="Relação entre população, armas de fogo e mortes violentas (Cluster 1)" width="500" height="300">


## 📊 Visualizações

A seguir, estão alguns dos gráficos mais relevantes gerados durante a análise:

- **Gráfico de Dispersão dos Clusters**: Mostrando a relação entre armas de fogo civis e mortes violentas por 100k habitantes em cada cluster.
- **Gráfico de Bolhas**: Comparação entre os clusters 1 e 4, destacando as diferenças no nível de violência e posse de armas civis.

📊 Principais Resultados: 
- O algoritmo identificou o número ideal de clusters (agrupamentos de países com características semelhantes) como sendo 6.
- Descobertas a partir desse breve estudo indicam que países com alta posse de armas nem sempre apresentam altas taxas de violência, destacando a complexidade do tema. 
- Também notamos padrões relacionados à geografia e às problemáticas jurídico-institucionais e socioeconômicos regionais. Nesse sentido, a América Latina apresenta um cenário único, com desafios estruturais que exacerbam a violência.
- Isso acarreta um padrão na região seguido sobretudo por países em que a questão do tráfico de drogas e do elevado domínio territorial por parte de criminosos aparece de maneira mais forte.
- Países como Brasil, Colômbia e El Salvador foram agrupados na cluster 4 pela máquina. Nesse grupo, o padrão que encontramos foram países latinos com população indo de médio a grande e níveis alarmantes de violência. 
- Países como a Áustria e a Finlândia, por sua vez, foram agrupados pelo algoritmo na cluster 0, em que tem-se países com baixíssima violência e população relativamente pequena. 

## 🚀 Próximos Passos

- Explorar as características institucionais e jurídicas de cada cluster.
- Expandir o modelo para incluir novas variáveis relacionadas sobretudo ao controle da criminalinalidade.


---

> *Este trabalho foi criado para inspirar os leitores mostrando a aplicação da ciência de dados em problemáticas do cotidiano. Espero que você encontre valor neste trabalho e utilize-o para aprimorar suas próprias pesquisas e projetos.
Paz 🖖* 🌟
