#Problema 1035 - BeeCrowd - Teste de Seleção

import math

valores = input().split(" ")
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

delta = b**2 - 4*a*c

if a != 0:
    if delta > 0:
        R1 = (-b + math.sqrt(delta))/(2*a)
        print("R1 = {:.5f}".format(R1))
        R2 = (-b - math.sqrt(delta))/(2*a)
        print("R2 = {:.5f}".format(R2))
    elif delta == 0:
        R1 = -b/(2*a)
        print("R1 = {:.5f}".format(R1))
        R2 = -b/(2*a)
        print("R2 = {:.5f}".format(R2))
    else:
        print("Impossivel de calcular")
else:
    print("Impossivel calcular")


