##### SUPONDO QUE JÁ TEMOS O VETOR estacao DETERMINADO: #####

# sorted(var)
# Criação da variável que comportará os valores das temperaturas #
ordem = []

# Variável que percorrerá todas as posições do vetor estacao #
i = 0
# As variáveis M e m indicarão as temperaturas máximas e mínimas dentro de cada posição do vetor estacao #

# Função looping que percorrerá as posições em estação, que é determinada com seu comprimento #
while i < len(estacao):

  # Função que add a informação selecionada no final do novo vetor ordem #
  # Coloquei int() só para os testes, mas o correto era float() #
  ordem.append(int(estacao[i][M]))
  ordem.append(int(estacao[i][m]))
  i = i + 1

# Função que coloca em ordem crescente as informações contidas no vetor ordem #
#sorted()

print("Lista com todas as temperaturas registradas em ordem crescente:")
print(sorted(ordem))
