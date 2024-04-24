install.packages("readxl")
library(readxl)
caminho <- "C:/Users/Vitória/Downloads/reg/countries.xlsx" ##localização do arquivo
dados <- read_excel(caminho)

##Coloco os valores da colunas xI e xL como numéricos, para evitar quaisquer problemas
dados$xI <- as.numeric(dados$xI)
dados$xL <- as.numeric(dados$xL)
##Crio um modelo de regressão
dados$Y <- dados$xI + dados$xL + rnorm(nrow(dados))

##Crio dois modelos de regressão simples:
regI <- lm(Y~xI, data=dados)
regL <- lm(Y~xL, data=dados)

##Crio um modelo de regressão múltiplo:
reg <- lm(Y~xI+xL, data=dados)

##Agora desenho o gráfico de cada modelo:

## 1- Modelos simples:
##1a) Usando o geom_smooth. Sintaxe: geom-smooth(method = "", formula = , se = FALSE, color = ""):

ggplot(dados, aes(x=xI, y=Y))+
geom_point()+
geom_smooth(method = "lm", formula = y~x, se = FALSE, color = "red")+
labs(x = "Innovation", y="Pib per", title = "Regress. Linear: Inovação x Pib per Capita")
##Resultado: 

##1b) Usando o geom_line:

dados$pred <- predict(regL) ##estimo os valores previstos para Yi no modelo Y~xL
ggplot(dados,aes(x=xL, y=Y))+
geom_point()+
geom_line(aes(y=pred), color="blue")+
labs(x="economic freedom", y="PIB per", title="Regress. Linear: Liberdade x PIB")



##2- Modelo Múltiplo:
ggplot(dados, aes(x = Y, y = predict(reg)))+
geom_point() +
geom_smooth(method = "lm", formula = y~x, se = FALSE, color = "navy") +
labs(x = "Valores Observados (Y)", y = "Valores Previstos (Y)", title = "Regress. Linear Múltpla: Innov+Freedom x PIB per")