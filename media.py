##### SUPONDO QUE JÁ TEMOS O VETOR estacao DETERMINADO: #####

  # Variável que percorrerá as posições do vetor estacao #
i = 0
  # Variável que selecionará sempre a posição onde se encontra a informação de temperatura máxima dentro do vetor de informações dos dias #
M = 1
  # Variável que selecionará sempre a posição onde se encontra a informação de temperatura mínima dentro do vetor de informações dos dias #
m = 2
  # Variável que armazenará as somas das temperaturas máximas #
SOMA = 0
  # Variável que armazenará as somas das temperaturas mínimas #
soma = 0

# Repetição que percorrerá todas as posições do vetor estacao #
          # A função 'len' foi usada pois assim o código funcionará para qualquer vetor #
for i in len(estacao):
  # estacao[i[M]] & estacao[i[m]] são as informações na posição do vetor dentro do vetor #
  SOMA = SOMA + estacao[i[M]]
  soma = soma + estacao[i[m]]
  i = i + 1

# Cálculo das médias #
MEDIA = SOMA / len(estacao)
media = soma / len(estacao)

print ("A média de temperaturas máximas no período eh: ", MEDIA)
print ("A média de temperaturas mínimas no período eh: ", media)