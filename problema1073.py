#Problema 1071 - BeeCrowd - Soma de Ímpares

N = int(input())
numero_testado = 0
for i in range(N):
    numero_testado = numero_testado+1
    resto = numero_testado % 2
    if resto == 0:
        potencia = numero_testado**2
        print("{}^2={}".format(numero_testado, potencia))
    
        

    






      
      



