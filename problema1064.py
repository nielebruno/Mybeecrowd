#Problema 1064

soma = 0
quantidade = 0

for i in range(6):
    numero = float(input())
    if numero > 0:
        soma = soma + numero
        quantidade = quantidade + 1

media = soma / quantidade
print("{} valores positivos".format(quantidade))
print("{:.1f}".format(media))
      
      



