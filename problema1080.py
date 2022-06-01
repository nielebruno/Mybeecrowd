#Problema 1080 - Maior e Posição

numeros = []
maior = 0
x = 0

for i in range (7):
    numeros.append(int(input()))
    if numeros[i] > maior:
        maior = numeros[i]
        x = i+1

print(maior)
print(x)
    
                  
    

