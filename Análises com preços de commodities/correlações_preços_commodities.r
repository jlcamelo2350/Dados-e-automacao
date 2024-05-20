# Armazenar os nomes das colunas de commodities em uma variável
colunas_commodities <- colnames(dados)[-1]

# Substituir valores NA pela média da coluna
for (coluna in colnames(dados)) {
  dados[[coluna]][is.na(dados[[coluna]])] <- mean(dados[[coluna]], na.rm = TRUE)
}

# Inicializar uma lista para armazenar as correlações
lista_correlacao <- list()

# Loop para calcular a correlação entre cada par de colunas:
for (i in 1:(length(colunas_commodities)-1)) {
  for (j in (i+1):length(colunas_commodities)) {
    correlacao <- cor(dados[[colunas_commodities[i]]], dados[[colunas_commodities[j]]])
    nome_correlacao <- paste(colunas_commodities[i], "vs.", colunas_commodities[j])
    lista_correlacao[[nome_correlacao]] <- correlacao
  }
}

# Converter a lista de correlações em um dataframe:
df_correlacoes <- do.call(rbind, lapply(names(lista_correlacao), function(x) {
  data.frame(pares = x, correlacao = lista_correlacao[[x]], stringsAsFactors = FALSE)
}))

# Exibir o dataframe com as correlações
print(df_correlacoes)
