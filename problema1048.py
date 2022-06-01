#Problema 1048 - Beecrowd - Aumento

salario = float(input())

if salario >= 0 and salario < 400.01:
    percentual = 15
elif salario >= 400.01 and salario < 800.01:
    percentual = 12
elif salario >= 800.01 and salario < 1200.01:
    percentual = 10
elif salario >= 1200.01 and salario <= 2000.00:
    percentual = 7
else:
    percentual = 4

reajuste = salario * percentual /100
novo_salario = salario + reajuste

print("Novo salario: {:.2f}". format(novo_salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("em percentual: {}%".format(percentual))
