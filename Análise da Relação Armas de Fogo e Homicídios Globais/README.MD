# 🔫 Armas de Fogo e Violência: Uma Análise Multifacetada da Relação entre Posse de Armas e Homicídios no Contexto Global

Este projeto explora a relação entre a posse de armas de fogo civis e a violência, especialmente as mortes violentas, em diferentes países ao redor do mundo. Utilizo uma abordagem baseada em aprendizado de máquina para agrupar países em clusters, a fim de identificar padrões e comportamentos semelhantes em relação à violência armada.

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

Gráfico interativo mostrando a relação entre população, armas de fogo civis e mortes violentas:
![Gráfico Interativo - Cluster 4](Análise da Relação Armas de Fogo e Homicídios Globais/gráficos/Relação entre população, armas de fogo e mortes violentas (Cluster 4).png)

#### Cluster 1: População Moderada e Baixa Violência
- **Países**: Exemplo de países.
- **Características**:
  - Países de diversos continentes.
  - Níveis moderados de posse de armas civis, porém, menores taxas de violência, em relação à cluster 4.

Gráfico de bolhas representando os países deste cluster:
(![Relação entre população, armas de fogo e mortes violentas (Cluster 1)](Análise da Relação Armas de Fogo e Homicídios Globais/gráficos/Relação entre população, armas de fogo e mortes violentas (Cluster 1).png)



## 📊 Visualizações

A seguir, estão alguns dos gráficos mais relevantes gerados durante a análise:

- **Gráfico de Dispersão dos Clusters**: Mostrando a relação entre armas de fogo civis e mortes violentas por 100k habitantes em cada cluster.
- **Gráfico de Bolhas**: Comparação entre os clusters 1 e 4, destacando as diferenças no nível de violência e posse de armas civis.

## 📈 Resultados

Os resultados indicam que países como o Brasil compartilham características de violência e posse de armas com outros países da América Latina, que enfrentam desafios críticos de segurança pública. Por outro lado, alguns países do cluster 1 demonstram maior controle tanto sobre a posse de armas quanto sobre as taxas de violência.

## 🚀 Próximos Passos

- Explorar as características institucionais e jurídicas de cada cluster.
- Estudar o impacto econômico e social da posse de armas e da violência.
- Expandir o modelo para incluir novas variáveis, como políticas de controle de armas.

## 🎯 Conclusão

Este estudo forneceu insights valiosos sobre a relação entre a posse de armas de fogo e a violência globalmente. Ele destaca a importância de políticas públicas robustas para combater o crescimento da violência armada e promover a segurança pública.

---

