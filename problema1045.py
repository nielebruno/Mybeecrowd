#Problema 1045 - Multiplos

valores = input().split(" ")
x = []

for i in range(len(valores)):
    x.append(float(valores[i]))

ordena = True

while ordena==True:
    ordena = False
    for i in range(len(x)-1):
        if x[i]< x[i+1]:
            a = x[i+1]
            x[i+1]=x[i]
            x[i]= a
            ordena = True
A = x[0]
B = x[1]
C = x[2]

if A >= (B+C):
    print("NAO FORMA TRINGULO")
elif A**2 == B**2 + C**2:
    print("TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2:
    print("TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
    print("TRIANGULO ACUTANGULO")

if A == B == C:
    print("TRIANGULO EQUILATERO")
elif (A == B) or (A == C) or (B == C):
    print("TRIANGULO ISOSCELES")

    
    


    
    

          



