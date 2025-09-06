# Classificação Histórica e Evolução de Clusters de Clientes 🛍️📊

Este projeto realiza uma análise detalhada da **base de clientes de uma marca do varejo**, utilizando regras de classificação personalizadas e visualizações para acompanhar a evolução de diferentes grupos de clientes ao longo do tempo (2021–2025).

---

## Objetivos 🎯
- Classificar clientes em diferentes grupos de valor e engajamento (FÃS, PREMIUM, SUPER VIP, VIP, POTENCIAL, BOM, OK, etc.).
- Acompanhar a evolução histórica desses grupos ao longo de 5 anos.
- Gerar insights estratégicos para **expansão consistente e sustentável** da marca.
- Identificar oportunidades de fidelização, conversão e reengajamento.

---

## Estrutura do Projeto 📑

### 1. Coleta de Dados 📊
- Dados de clientes e vendas obtidos a partir de tabelas de um banco SQL Server.  
- Os nomes originais das tabelas foram **anonimizados** para este repositório, mantendo apenas a lógica.

### 2. Classificação de Clientes 🏷️
- Implementada em Python, com thresholds de valor e frequência ajustáveis.  
- Clientes são classificados em categorias como:
  - **01 - FÃS**
  - **02 - PREMIUM**
  - **03 - SUPER VIP**
  - **04 - VIP**
  - **05 - POTENCIAL**
  - **06 - BOM**
  - **07 - OK**
  - **10 - NEW BUYERS**
  - **11 - ONE TIME BUYERS**
  - **20 - INATIVOS HP**
  - **21 - INATIVOS RECENTES**
  - **22 - PERDIDOS**
  - **23 - NUNCA COMPROU**

### 3. Análise Histórica ⏳
- As classificações são calculadas ano a ano (2021–2025).
- É gerado um DataFrame consolidado com a evolução de cada cliente.

### 4. Visualização 📈
- Gráficos interativos em **Plotly** permitem:
  - Ver a evolução de cada cluster em subplots individuais.
  - Comparar todos os clusters em um único gráfico agrupado.
- Estatísticas resumo identificam os grupos com **maior crescimento** ao longo do tempo.

---

## Resultados Gráficos 📊
Os gráficos mostram:
- Crescimento consistente dos clusters de **FÃS** e **PREMIUM** ✅  
- Estabilidade em **VIP** e **SUPER VIP** 📉➡️📈  
- Expansão gradual dos grupos intermediários (**POTENCIAL, BOM, OK**) 🔄  
- Presença constante de **NEW BUYERS** e **ONE TIME BUYERS**, garantindo renovação da base 🔄  
- Aumento esperado dos **INATIVOS** e **PERDIDOS**, apontando necessidade de estratégias de reengajamento ⚠️  

---

## Conclusões 🎓
- A marca vem crescendo de forma **sólida e sustentável**, sem movimentos artificiais.  
- **Fidelização** é o motor principal (crescimento de FÃS e PREMIUM).  
- Há **grande espaço para conversão** dos clientes intermediários.  
- Estratégias de **winback** podem reduzir o avanço dos inativos.  

👉 Em resumo: o crescimento é **consistente**, equilibrando aquisição, retenção e fidelização.  

---

## Tecnologias Utilizadas 🛠️
- **Python**: Automação e análise de dados.  
- **Pandas**: Manipulação e tratamento de dados.  
- **PyODBC**: Conexão com banco SQL Server.  
- **Plotly (Express & Graph Objects)**: Visualização interativa.  
- **Logging**: Monitoramento do processo.  

---

## Contato 📧
Dúvidas ou sugestões? Entre em contato: **jlcam3250@gmail.com**

Este projeto foi criado para **inspirar análises de dados no varejo**, ajudando a transformar informação em estratégia.  
Espero que você encontre valor neste trabalho e que ele possa servir como base para seus próprios estudos e projetos.  

Paz 🖖🌟

