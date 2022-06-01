#Problema 1012 - Área - BeeCrowd

entrada = input().split(" ")

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

MaiorAB = int(((a+b) + abs(a-b))/2)
MaiorAB_C = int(((MaiorAB + c) + abs(MaiorAB - c))/2)

print("{} eh o maior".format(MaiorAB_C))
