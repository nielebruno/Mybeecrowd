#Problema 1070 - BeeCrowd - 6 números ímpares

numero = int(input())
i = 0
cont = 1

while cont <= 6:
    numero_testado = numero + i
    resto = numero_testado % 2
    if resto != 0:
        cont = cont + 1
        print(numero_testado)
    i = i + 1






      
      



