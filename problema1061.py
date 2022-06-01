#Problema 1061

dia_vetor0 = input().split(" ")
dia_inicio = int(dia_vetor0[1])

horario_inicio = input().split(":")
hora_inicio = int(horario_inicio[0])
minuto_inicio = int(horario_inicio[1])
segundo_inicio = int(horario_inicio[2])
  
dia_vetor1 = input().split(" ")
dia_termino = int(dia_vetor1[1])

horario_termino = input().split(":")
hora_fim = int(horario_termino[0])
minuto_fim = int(horario_termino[1])
segundo_fim = int(horario_termino[2])

dias_em_seg_inicio = dia_inicio * 24 * 60 * 60
horas_em_seg_inicio = hora_inicio * 60 * 60
minutos_em_seg_inicio = minuto_inicio * 60

dias_em_seg_fim = dia_termino * 24 * 60 * 60
horas_em_seg_fim = hora_fim * 60 * 60
minutos_em_seg_fim = minuto_fim * 60


tempo_inicio = dias_em_seg_inicio + horas_em_seg_inicio + minutos_em_seg_inicio + segundo_inicio
tempo_fim = dias_em_seg_fim + horas_em_seg_fim + minutos_em_seg_fim + segundo_fim

duracao = tempo_fim - tempo_inicio

dias = duracao // 86400
print("{} dia(s)".format(dias))
resto_dias = duracao % 86400

horas = resto_dias // 3600
print("{} hora(s)".format(horas))
resto_horas = resto_dias % 3600

minutos = resto_horas // 60
print("{} minuto(s)".format(minutos))

segundos = resto_horas % 60
print("{} segundo(s)".format(segundos))
      
      



