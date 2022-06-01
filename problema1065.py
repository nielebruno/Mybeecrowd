#Problema 1064

quantidade = 0

for i in range(5):
    numero = int(input())
    resto = numero % 2
    if resto == 0:
        quantidade = quantidade + 1

print("{} valores positivos".format(quantidade))

      
      



