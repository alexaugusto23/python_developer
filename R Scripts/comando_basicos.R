# Aprender comando básicos R

# Usar o R como calculadora.

5 + 5
5 - 2
5 * 2
8 / 4
5 ^ 2
25 ^ 0.5
sqrt(25)
(5+5) + (10-5)

# Criando Objetos
a=5
b=6
a * b

# Criando Vetores
# c() função concatenar
nomes =  c("João", "Maria", "Lucas", "Jose")
notas =  c(22,21,10,5)
mode(nomes)
mode(notas)

# Documentação das funções
?mode

# Tamanho do vetor
length(notas)

# Valor mínimo
min(notas)

# Valor máximo
max(notas)

# Média
mean(notas)

# Variância
var(notas)

# Desvio Padrão
var(notas)^0.5
sd(notas)

# Coeficiente de Variação
100 * sd(notas) / mean(notas)

# Função para obter Coeficiente de Variação
cv=function(notas) {100 * sd(notas) / mean(notas)}
cv(notas)
notas

# Criando amostras
sample(notas)
?sample

# Vetores com sequência
1:10
seq(1,10, l=10)
seq(1,10, by=0.15)

# Vetor com String
paste("Prova", 1:4)

# Criar Matrizes
Joao=c(10,15,20,25)
Maria=c(5,20,25,3)
Lucas=c(10,12,18,5)
Jose=c(20,25,22,23)

cbind(Joao, Maria, Lucas, Jose) # Coloca um vetos na frente de outro.
rbind(Joao, Maria, Lucas, Jose)  # Coloca um vetos na abaixo de outro.

Mat = rbind(Joao, Maria, Lucas, Jose)
Mat

rownames(Mat) # Ver nome das linhas
colnames(Mat) # Ver nome das colunas

colnames(Mat) = paste("Prova", 1:4)
Mat

# Funções de Agregação de matrizes
colSums(Mat) # soma das linhas
colMeans(Mat) # média das linhas

rowSums(Mat) # soma das linhas
rowMeans(Mat) # média das linhas

# Função Apply 1 operações por linha
apply(Mat, 1, max)
apply(Mat, 1, min)
apply(Mat, 1, mean)
apply(Mat, 1, var)
apply(Mat, 1, sd)
apply(Mat, 1, cv)

# Função Apply 2 operações por coluna
apply(Mat, 2, max)
apply(Mat, 2, min)
apply(Mat, 2, mean)
apply(Mat, 2, var)
apply(Mat, 2, sd)
apply(Mat, 2, cv)

matrix(c(10,20,15,5,3,8,9,2), ncol=2)
matrix(c(10,20,15,5,3,8,9,2), ncol=2, byrow=TRUE)

