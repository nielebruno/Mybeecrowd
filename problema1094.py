#Problema 1094 - Experiências

N = int(input())
total = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

#Entrada de dados e contagem
for i in range (N):
    quantias_tipos = input().split(" ")
    quantidade = int(quantias_tipos[0])
    tipo = quantias_tipos[1]
    total = total + quantidade
    if tipo == 'C':
        total_coelhos = total_coelhos + quantidade
    elif tipo == 'R':
        total_ratos = total_ratos + quantidade
    else:
        total_sapos = total_sapos + quantidade

#cálculos dos percentuais testados de cada animal:
percentual_coelhos = (total_coelhos/total) * 100
percentual_ratos = (total_ratos/total) * 100
percentual_sapos = (total_sapos/total) * 100

#impressão dos resultados
print("Total:{} cobaias".format(total))
print("Total de coelhos:{}".format(total_coelhos))
print("Total de ratos:{}".format(total_ratos))
print("Total de sapos:{}".format(total_sapos))

print("Percentual de coelhos:{:.2f}%".format(percentual_coelhos))      
print("Percentual de ratos:{:.2f}%".format(percentual_ratos))
print("Percentual de sapos:{:.2f}%".format(percentual_sapos))
