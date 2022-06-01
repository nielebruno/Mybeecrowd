#Problema 1050 - Beecrowd - DDD

ddd = int(input())

if ddd == 61:
    destination = "Brasilia"
elif ddd == 71:
    destination = "Salvador"
elif ddd == 11:
    destination = "Sao Paulo"
elif ddd == 21:
    destination = "Rio de Janeiro"
elif ddd == 32:
    destination = "Juiz de Fora"
elif ddd == 19:
    destination = "Campinas"
elif ddd == 27:
    destination = "Vitoria"
elif ddd == 31:
    destination = "Belo Horizonte"
else:
    destination = "DDD nao cadastrado"

print(destination)
