#Problema 1046 - Beecrowd - Tempo de Jogo

hora = input().split(" ")
inicio = int(hora[0])
fim = int(hora[1])

if inicio > fim:
    ate_meia_noite = 24 - inicio
    meia_noite_em_diante = fim
    duracao = ate_meia_noite + meia_noite_em_diante
    print("O JOGO DUROU {" "} HORA(S)".format(duracao))
elif inicio == fim:
    duracao = 24
    print("O JOGO DUROU {" "} HORA(S)".format(duracao))
elif inicio < fim:
    duracao = fim - inicio
    print("O JOGO DUROU {" "} HORA(S)".format(duracao))
