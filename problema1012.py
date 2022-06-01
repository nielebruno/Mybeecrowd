#Problema 1012 - Área - BeeCrowd

entrada = input().split(" ")

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

pi = 3.14159

area_triangulo = (A*C)/2
print("TRIANGULO:{:.3f}".format(area_triangulo))

area_circulo = pi*(C**2)
print("CIRCULO:{:.3f}".format(area_circulo))

area_trapezio = (A+B)*C/2
print("TRAPEZIO:{:.3f}".format(area_trapezio))

area_quadrado = B**2
print("QUADRADO:{:.3f}".format(area_quadrado))

area_retangulo = A*B
print("RETANGULO:{:.3f}".format(area_retangulo))
