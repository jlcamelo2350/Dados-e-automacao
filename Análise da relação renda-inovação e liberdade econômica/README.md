# 🌐 Impactos da Inovação e da Liberdade Econômica na Renda Per Capita: Uma Análise Regressiva 🌍

## 📝 Resumo

Este repositório apresenta um modelo de regressão múltipla que investiga a relação entre a renda per capita (PPC), a inovação (xI) e a liberdade econômica (xL) de 129 países. O modelo revela que tanto a inovação quanto a liberdade econômica impactam positivamente PIB per Capita PPC, com a inovação mostrando um efeito mais forte.

---

## 📁 Estrutura do Repositório

- **README.md**: Este arquivo (que você está lendo!) fornece uma visão geral do projeto, metodologia, resultados e conclusões.
- **data.csv**: Contém os dados utilizados para a análise, incluindo PPC, Inovação e Liberdade Econômica para cada país.
- **analysis.ipynb**: Notebook Jupyter com a implementação completa da análise, incluindo exploração de dados, modelagem de regressão e visualizações.

---

## 🔍 Metodologia

1. **Coleta de Dados**: Dados obtidos do Banco Mundial (e outras fontes como estimativas até da CIA (para a Coréia do Norte), o Índice de Liberdade Econômica e o Índice de Inovação.

1.1 **Veja os dados:**
*   1.1.1 - PIB per Capita PPC, World Bank: https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD
*   1.1.2 - Economic Freedom Index: https://www.heritage.org/index/pages/all-country-scores
*   1.1.3 - Innovation Index: https://www.wipo.int/edocs/pubdocs/en/wipo-pub-2000-2023-section1-en-gii-2023-at-a-glance-global-innovation-index-2023.pdf
3. **Análise Exploratória de Dados**: Análise de medidas descritivas e visualizações gráficas para identificar padrões e relações entre as variáveis.
4. **Modelagem de Regressão Múltipla**:
    - Ajuste de modelos de regressão linear simples e múltipla para entender a relação entre as variáveis.
    - Verificação de multicolinearidade, normalidade dos resíduos, homocedasticidade e heterocedasticidade.
    - Ajuste do modelo final com erros padrão robustos para lidar com a heterocedasticidade.
5. **Interpretação dos Resultados**:
    - Análise de coeficientes, R-squared, significância estatística e visualizações para interpretar os resultados do modelo.

---

## 📊 Resultados

- A inovação e a liberdade econômica têm impactos positivos e significativos no PIB per Capita PPC.
- A inovação tem um impacto maior na PIB per Capita PPC do que a liberdade econômica.
- O modelo explica aproximadamente 78,4% da variabilidade da PIB per Capita PPC.

---

## 🔗 Conclusão

Este estudo destaca a importância da inovação e da liberdade econômica para o crescimento e desenvolvimento econômico. As descobertas são valiosas para formuladores de políticas que buscam promover o bem-estar de seus cidadãos.

---

## ⚠️ Limitações do Trabalho

1. **Grau de Desenvolvimento Econômico**: O grau de desenvolvimento econômico e outras características (como crescimento, cenários macro e microeconômicos) influenciam o grau de inovação tecnológica de um país, conforme diversos estudos. Por exemplo, países como Brasil, China e Índia, que são de renda média, apresentam desempenhos em inovação acima do esperado. O desenvolvimento econômico é um fenômeno construído ao longo do tempo, e nossa modelagem não captura isso adequadamente, pois utiliza dados apenas do ano passado e não de uma série temporal. Estudos futuros deveriam considerar uma longa série temporal para obter resultados mais precisos. Isto é, seria necessário realizar essa modelagem ao longo do tempo para verificar se a inovação e a liberdade econômica influenciam a renda positiva ou negativamente nesse período.

2. **Inovação**: Este estudo sugere que a inovação explica grande parte da renda per capita de um país. No entanto, isso pode ser uma falha do estudo, pois o potencial da inovação para explicar a renda per capita pode estar sendo superestimado. A hipótese mais convincente é que alguns fatores que explicam a alta renda de um país são os mesmos que levam a uma alta inovação. Por exemplo, países com educação de alto nível e forte integração entre academia e empresas tendem a ter maior renda e também maior inovação. Dessa forma, a variável educação afeta positivamente tanto a renda quanto a inovação. Portanto, a afirmação de que a inovação influencia significativamente a renda de um país é válida, mas deve-se considerar que essa influência pode estar sendo aumentada neste modelo.

3. **Liberdade Econômica**: Países mais desenvolvidos tendem a se tornar mais livres ao longo do tempo. Assim, a liberdade econômica pode ser um reflexo do grau de desenvolvimento de um país e não necessariamente a causa de um elevado PIB per capita. Devido à falta de dados sobre a variação da liberdade econômica ao longo do tempo, a relação entre liberdade econômica e PIB per capita pode estar sendo superestimada. Isso não invalida os resultados, mas deve ser considerado.

4. **Complexidade Econômica**: A economia envolve uma interação complexa entre milhares de variáveis que não podem ser captadas por um único modelo. Esta modelagem focou em aspectos específicos, não na totalidade. Considere isso ao interpretar os resultados.

---


## 📈 Próximos Passos

- Explorar outras variáveis que podem influenciar o PIB per Capita.
- Analisar a relação entre PIB per Capita PPC, inovação e liberdade econômica ao longo do tempo.

---

## 📝 Observações

- Este repositório é para fins educacionais e de pesquisa.
- Os dados utilizados são de livre acesso e podem ser encontrados nas fontes mencionadas.
- O código Python no notebook Jupyter pode ser facilmente adaptado para outras análises.

---

## 🙏 Agradecimentos

Agradeço aos autores dos dados utilizados nesta análise.

---

## 📬 Contato

Para qualquer dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo.

---

> *Este repositório foi criado para inspirar e facilitar a análise econômica. Espero que você encontre valor neste trabalho e utilize-o para aprimorar suas próprias pesquisas e projetos.* 🌟

