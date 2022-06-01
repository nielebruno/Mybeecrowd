#Problema 1019 - BeeCrowd - Conversão de Tempo

N = int(input())

horas = N//3600
resto_horas = N % 3600

minutos = resto_horas//60
resto_minutos = resto_horas%60

segundos = resto_minutos

print("{}:{}:{}".format(horas, minutos, segundos))

