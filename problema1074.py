#Problema 1074 - BeeCrowd - Par ou Ímpar

N = int(input())


for i in range(N):
    numero_testado = int(input())
    resto = numero_testado % 2
    if numero_testado == 0:
        print("NULL")
    elif numero_testado > 0:
        if resto == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else:
        if resto == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
        
        
        
    
        

    






      
      



