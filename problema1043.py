#Problema 1043 - Triangulo

valores = input().split(" ")
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

if (A+B)>C and (A+C)>B and (B+C)>A:
    perimetro = A+B+C
    print("Perímeto = {:.1f}".format(perimetro))
else:
    area_trapezio = ((A+B)*C)/2
    print("Area = {:.1f}".format(area_trapezio))


    

          



