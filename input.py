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

print(estacao)
