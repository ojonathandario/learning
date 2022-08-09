def main():
  
  input_estacao()

  contador_chuva()

  medias_temperaturas()

  ordem_temperaturas()


                  #### INPUT DOS DADOS ####

def input_estacao():
  
  indicador_dia = 1

  estacao = []
    

  # Coloquei 4 para testar 3 vetores. Agora é só colocar 366 e brincar com valores do ano todo! #
  while indicador_dia < 4:

    print("digite as informações do dia ", indicador_dia)

    informacoes = [
      input("Chuveu? S ou N?: "),
      input("Digite a temperatua máxima: "),
      input("Digite a temperatura mínima: ")
    ]

    estacao.insert(indicador_dia - 1, informacoes)
    #ou
    #estacao.append(informacoes);
    indicador_dia = indicador_dia + 1

  # Imprimir o vetor estação para conferir #
  #print(estacao)

  
  
                  #### CONTADOR DOS DIAS DE CHUVA ####

def contador_chuva():
    
  posicao_vetor_estacao = 0

  posicao_informacao_chuva = 0

  count_chuva = 0

  count_n_chuva = 0


  while posicao_vetor_estacao < len(estacao):

    if estacao [posicao_vetor_estacao][posicao_informacao_chuva] == 'S':
      count_chuva = count_chuva + 1
    else:
      count_n_chuva = count_n_chuva + 1
        
    posicao_vetor_estacao = posicao_vetor_estacao + 1
      
      
  print ("Quantidade de dias de chuva: ", count_chuva)




                  #### CÁLCULO DAS MÉDIAS DE TEMPERATURAS ####

def medias_temperaturas():
    
  posicao_vetor_estacao = 0

  posicao_temperatura_maxima = 1

  posicao_temperatura_minima = 2

  SOMA_TEMPERATURA_MAXIMA = 0

  soma_temperatura_minima = 0


  while posicao_vetor_estacao < len(estacao):
    # Coloquei int() só para os testes, mas o correto era float() #
    SOMA_TEMPERATURA_MAXIMA = SOMA_TEMPERATURA_MAXIMA + int(estacao[posicao_vetor_estacao][posicao_temperatura_maxima])
    soma_temperatura_minima = soma_temperatura_minima + int(estacao[posicao_vetor_estacao][posicao_temperatura_minima])

    posicao_vetor_estacao = posicao_vetor_estacao + 1
      

  MEDIA_TEMPERATURA_MAXIMA = SOMA_TEMPERATURA_MAXIMA / len(estacao)
  media_temperatura_minima = soma_temperatura_minima / len(estacao)

  print ("A média de temperaturas máximas no período eh: ", MEDIA_TEMPERATURA_MAXIMA)
  print ("A média de temperaturas mínimas no período eh: ", media_temperatura_minima)



                  #### TEMPERATURAS EM ORDEM CRESCENTE ####

def ordem_temperaturas():
    
  temperaturas = []

  posicao_vetor_estacao = 0


  while posicao_vetor_estacao < len(estacao):

    ordem.append(int(estacao[posicao_vetor_estacao][posicao_temperatura_maxima]))
    ordem.append(int(estacao[posicao_vetor_estacao][posicao_temperatura_minima]))

    posicao_vetor_estacao = posicao_vetor_estacao + 1

  # Função que coloca em ordem crescente as informações contidas no vetor ordem #
    #sorted()

  print("Lista com todas as temperaturas registradas em ordem crescente:")
  print(sorted(temperaturas))



main()
