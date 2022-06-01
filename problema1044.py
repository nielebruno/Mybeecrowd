#Problema 1044 - Multiplos

valores = input().split(" ")
A = float(valores[0])
B = float(valores[1])

if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

resto = maior % menor

if resto == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")




    

          



