library(readxl)  # Carrega a biblioteca `readxl` para leitura de arquivos Excel
library(ggplot2) # Carrega a biblioteca `ggplot2` para criação de gráficos

# Define o local onde está o arquivo Excel
caminho <- 'C:/Users/Camelo/Downloads/commodities(1).xlsx'

# Lê o conteúdo do arquivo Excel em um data frame
dados <- read_excel(caminho)

# Extrai os nomes das commodities (exceto a primeira coluna (data))
commodities <- colnames(dados)[-1]

# Loop para criar gráficos de cada commodity
for(commodity in commodities) {
  graph <- ggplot(dados, aes(x = index, y = !!sym(commodity))) 
    + geom_area(fill = "navy") 
  
    # Define os títulos e rótulos dos eixos: título e nome dos eixos
    + labs(title = paste("Preço da Commodity", commodity, "ao Longo do Tempo"),
           x = "Data", y = "Preço da Commodity") 
    
    # Aplica um tema minimalista ao gráfico
    + theme_minimal()
  
  # Imprime o gráfico na tela
  print(graph)
}
