## É o código utilizado para rodar a modelagem estatística apresentada no artigo Inovação, 
##liberdade econômica e renda per capita
##disponível aqui nesse mesmo github, no repositório economics.

# Instala e carrega a biblioteca readxl para leitura de arquivos do Excel
install.packages("readxl")
library(readxl)
#Instala e carrega a biblioteca ggplot2 para gráficos
install.packages("ggplot2")
library(ggplot2)

# Define o caminho do arquivo Excel a ser lido
caminho <- "C:/Users/Alves/Downloads/reg/countries.xlsx" ##local onde está armazenado a tabela que utilizei para a modelagem

# Lê os dados do arquivo Excel
dados <- read_excel(caminho)

# Converte as colunas xI e xL para numérico para evitar problemas
dados$xI <- as.numeric(dadosxL <- as.numeric(dados$xL)

# Cria-se o modelo de regressão com Y sendo a variável dependente, as colunas xI, xL 
#contendo os valores das variáveis independentes e um erro randômico (rnorm)
dadosxI + dados$xL + rnorm(nrow(dados))

# Cria modelos de regressão simples
regI <- lm(Y ~ xI, data = dados) ##Y como variável dependente e xI como variável independente
regL <- lm(Y ~ xL, data = dados)

# Mostra na tela os resultados da regressão simples (RLS):
summary(regI)
summary(regL)

# Cria um modelo de regressão múltipla
reg <- lm(Y ~ xI + xL, data = dados)

#Mostra na tela os resultados da RLM(múltipla):
summary(reg)


# Gráficos dos modelos:
# Modelo simples usando geom_smooth:
ggplot(dados, aes(x = xI, y = Y)) +
  geom_point() +
  geom_smooth(method = "lm", formula = y ~ x, se = FALSE, color = "red") +
  labs(x = "Inovação", y = "PIB per capita", title = "Regressão Linear: Inovação x PIB per Capita")