##### SUPONDO QUE JÁ TEMOS O VETOR estacao DETERMINADO: #####


# Variável resposável a percorrer todas as posições do vetor estacao #
i = 0
    # Variável indicadora da posição da informação a ser verificada #
j = 0
    # Variável que contará quantas vezes a verificação for positiva #
count = 0
    # Variável que contará quantas vezes a verificação for falsa (sei que não precisa)
ncount = 0

# Repetição para percorrer todas as posições do vetor estacao #
while i < len(estcao):

  # Verificação da condicional se choveu ou não #
  if estacao [i][j] == 'S':
    count = count + 1
  else:
    ncount = ncount + 1
  i = i + 1
  
print ("Quantidade de dias de chuva: ", count)
