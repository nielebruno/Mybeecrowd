#Problema 1071 - BeeCrowd - Soma de Ímpares

X = int(input())
Y = int(input())

if X > Y:
    numero1 = Y
    numero2 = X
else:
    numero1 = X
    numero2 = Y

j = numero1
soma = 0

while j < (numero2-1):
    numero_testado = j+1
    resto = numero_testado % 2
    if resto != 0:
        soma = soma + numero_testado
    j = j + 1
        
print(soma)
    






      
      



