#Problema 1018 - BeeCrowd - Gasto Gasolina

nota = int(input())
print(nota)

listacedulas = [100,50,20,10,5,2,1]

for i in range(len(listacedulas)):
    cedulaAtual = listacedulas[i]
    numero_cedulas = nota//cedulaAtual
    print("{} nota(s) de R$ {},00".format(numero_cedulas,cedulaAtual))
    nota = nota % cedulaAtual
           
