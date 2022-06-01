#Problema 1047 - Beecrowd - Tempo de Jogo

hora = input().split(" ")
hora_inicio = int(hora[0])
minutos_inicio = int(hora[1])
hora_fim = int(hora[2])
minutos_fim = int(hora[3])

if hora_inicio > hora_fim:
    ate_meia_noite = 24 - inicio
    meia_noite_em_diante = fim
    duracao_horas = ate_meia_noite + meia_noite_em_diante
    if minutos_inicio == minutos_fim:
        duracao_minutos = minutos_inicio - minutos_fim
        print("O JOGO DUROU {" "} HORA(S) e {" "} MINUTOS".format(duracao_horas,duracao_minutos))
    else:
        duracao_minutos = minutos_fim - minutos_inicio
        print("O JOGO DUROU {" "} HORA(S) e {" "} MINUTOS".format(duracao_horas,duracao_minutos))
elif (hora_inicio == hora_fim) and (minutos_inicio == minutos_fim):
    duracao_horas = 24
    if minutos_inicio == minutos_fim:
        duracao_minutos = minutos_inicio - minutos_fim
        print("O JOGO DUROU {" "} HORA(S) e {" "} MINUTOS".format(duracao_horas,duracao_minutos))
    else:
        duracao_minutos = minutos_fim - minutos_inicio
        print("O JOGO DUROU {" "} HORA(S) e {" "} MINUTOS".format(duracao_horas,duracao_minutos))
elif hora_inicio < hora_fim:
    duracao_horas = hora_fim - hora_inicio
    duracao_minutos = minutos_fim - minutos_inicio
    print("O JOGO DUROU {" "} HORA(S) E {" "} MINUTO(S)".format(duracao_horas,duracao_minutos))
