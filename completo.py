                  #### INPUT DOS DADOS ####

# Variável de controle de quantidade de repetições e posições #
i = 1

# Definição da variável que armazenará os dados da estação #
estacao = []

# Repetição para alimentação das informações diárias da variável estacao #
while i < 3:

    # Indicador do dia que receberá os dados #
    print("digite as informações do dia ", i)

    # Variável sendo preenchida com as informações diárias #
    dia = [
        input("Chuveu? S ou N?: "),
        input("Digite a temperatua máxima: "),
        input("Digite a temperatura mínima: ")
    ]

    # Variável estacao sento alimentada: cada posição com uma lista de informações #
    estacao.insert(i - 1, dia)
    #ou
    #estacao.append(dia);
    i = i + 1
    # controle de quantas posições serão armazenadas na variável estacao #

# print(estacao)

  
                  #### CONTADOR DOS DIAS DE CHUVA ####

  
# Variável resposável a percorrer todas as posições do vetor estacao #
i = 0
    # Variável indicadora da posição da informação a ser verificada #
j = 0
    # Variável que contará quantas vezes a verificação for positiva #
count = 0
    # Variável que contará quantas vezes a verificação for falsa (sei que não precisa)
ncount = 0

# Repetição para percorrer todas as posições do vetor estacao #
while i < len(estacao):

  # Verificação da condicional se choveu ou não #
  if estacao [i[j]].value == s:
  count = count + 1
  else:
  ncount = ncount + 1
  i = i + 1
  
print ("Quantidade de dias de chuva: ", count)


                  #### CÁLCULO DAS MÉDIAS DE TEMPERATURAS ####

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



                  #### TEMPERATURAS EM ORDEM CRESCENTE ####

