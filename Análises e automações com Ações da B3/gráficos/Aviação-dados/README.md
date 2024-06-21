### **Análise do Setor de Aviação: Boeing vs. Airbus vs. Embraer**

Introdução

Realizou-se uma análise abrangente do setor de aviação, comparando as ações da Embraer (EMBR3), Boeing (BA) e Airbus (EADSY) no período de 2017 a 2024. O objetivo é fornecer insights sobre o desempenho das empresas e as tendências do mercado.

Bibliotecas Importadas
Python

import seaborn as sns
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

Funções Criadas

    dados_preços(): Essa função baixa os dados históricos de preços das ações da Embraer do Yahoo Finance e os armazena em um DataFrame.

    preços_concorrentes(): Similar à função anterior, essa função baixa os dados de preços das ações da Boeing e Airbus no mesmo período.

Análise da Embraer

1. Preços das Ações ao Longo do Tempo

    O gráfico de dispersão com linhas mostra uma tendência de crescimento geral das ações da Embraer entre 2017 e 2024, com algumas flutuações ao longo do caminho.
    Uma linha de tendência curva é adicionada para destacar a tendência geral de crescimento.

2. Distribuição dos Preços das Ações

    O histograma de dispersão revela que a distribuição dos preços das ações da Embraer está concentrada entre 15 e 20 reais por ação.

3. Preços Médios Anuais

    O gráfico de dispersão com linha mostra a evolução dos preços médios anuais das ações da Embraer.
    Observa-se uma queda significativa em 2020 (ano da pandemia) e uma recuperação subsequente nos anos seguintes.

4. Comportamento Anual dos Preços

    O gráfico FacetGrid permite visualizar o comportamento individual dos preços das ações da Embraer em cada ano.
    É possível identificar períodos de estabilidade, crescimento e queda ao longo do tempo.

5. Métricas Adicionais

    Alguns cálculos de estatísticas básicas.

Análise da Boeing

1. Preços das Ações ao Longo do Tempo

    O gráfico de dispersão com linhas mostra uma forte subida dos preços das ações da Boeing entre 2017 e 2018, seguida por uma queda em 2020 e uma recuperação gradual nos anos seguintes.
    Uma linha de tendência curva é adicionada para destacar a tendência geral de crescimento.

2. Distribuição dos Preços das Ações

    O histograma de dispersão revela que a distribuição dos preços das ações da Boeing está mais concentrada do que a da Embraer, com a maioria dos preços na faixa de 200 a 350 reais por ação.

3. Variabilidade dos Preços das Ações

    O desvio padrão dos preços da Boeing foi de R$ 77,69, indicando uma volatilidade significativamente maior do que a da Embraer.

4. Análise Detalhada do Comportamento

    A análise do gráfico e das métricas adicionais revela que a Boeing teve um período de forte crescimento entre 2017 e 2018, seguido por um impacto negativo da pandemia em 2020.
    A recuperação da empresa foi mais lenta do que a da Embraer, e o preço das ações ainda não atingiu os níveis pré-pandemia.

Análise da Airbus

1. Preços das Ações ao Longo do Tempo

*   O gráfico de dispersão com linhas mostra uma tendência de crescimento consistente das ações da Airbus entre 2017 e 2020, seguida por uma queda em 2020 e uma recuperação em forma de "V" em 2021.
*   A partir de 2022, a empresa retoma a trajetória de crescimento.
    Uma linha de tendência curva é adicionada para destacar a tendência geral de crescimento.

2. Distribuição dos Preços das Ações

*    O histograma de dispersão revela que a distribuição dos preços das ações da Airbus é mais concentrada do que a da Boeing, com a maioria dos preços na faixa de 10 a 20 euros por ação.
   
3. Variabilidade dos Preços das Ações

*    O desvio padrão dos preços da Airbus foi de R$ 6,42, indicando uma volatilidade menor do que a da Boeing e similar à da Embraer.

4. Análise Detalhada do Comportamento

*    A análise do gráfico e das métricas adicionais revela que a Airbus teve um período de crescimento consistente entre 2017 e 2020, com um impacto negativo da pandemia em 2020.
*    A empresa se recuperou rapidamente em 2021 e retomou a trajetória de crescimento nos anos seguintes.
*    A Airbus demonstra maior resiliência à volatilidade do mercado em comparação com a Boeing.

5. Comportamento Anual dos Preços

*    O gráfico FacetGrid permite visualizar o comportamento individual dos preços das ações da Airbus em cada ano.
*    É possível identificar períodos de crescimento constante, queda em 2020 e recuperação em 2021, seguido por crescimento nos anos seguintes.

**Considerações Finais**

*    As três empresas analisadas (Embraer, Boeing e Airbus) apresentaram diferentes trajetórias de preços no período de 2017 a 2024.
*    A Embraer teve um crescimento moderado com volatilidade média. A Boeing, por sua vez, experimentou um forte crescimento inicial seguido de queda significativa e recuperação gradual, pós pandemia, seguida de nova queda agora em 2024. Ou seja, a Boeing parece estar instável, devido a seu futuro ainda incerto e problemas apresentados. A Embraer e Airbus agradecem.
*    A Airbus se destacou por sua resiliência à volatilidade, com crescimento consistente até 2020, recuperação --mais veloz que as concorrentes-- no pós pandemia e retomada do crescimento nos anos seguintes.
*    É importante ressaltar que essa análise é baseada em dados históricos e não garante previsões futuras.
    Recomenda-se realizar análises mais aprofundadas e considerar outros fatores antes de tomar decisões de investimento.

Próximos Passos

    Analisar outros indicadores financeiros das empresas, como lucratividade, dívida e fluxo de caixa.
    Avaliar as perspectivas futuras das empresas, considerando fatores como lançamentos de novos produtos, estratégias de mercado e cenário macroeconômico.
    Combinar a análise fundamental com a análise técnica para obter uma visão mais completa do potencial de investimento em cada empresa.

Observações

    O código Python completo para a análise pode ser encontrado no repositório GitHub.
    Este resumo fornece uma visão geral dos resultados da análise. Para detalhes mais aprofundados, consulte o código e os gráficos.
    É importante lembrar que o mercado de ações é complexo e envolve riscos. Consulte um profissional financeiro antes de tomar qualquer decisão de investimento.

Recursos Adicionais

    Yahoo Finance: https://br.finance.yahoo.com/
    Investing.com: https://pt.investing.com/
    B3: https://www.b3.com.br/

Espero que esta análise tenha sido útil e informativa.

Fique à vontade para fazer perguntas ou solicitar mais informações.
