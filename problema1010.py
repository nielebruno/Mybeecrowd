#Beecrowd - Problema 1010

linha1 = input().split(" ")
linha2 = input().split(" ")

codigo1 = int(linha1[0])
numero1 = int(linha1[1])
valor1 = float(linha1[2])

codigo2 = int(linha2[0])
numero2 = int(linha2[1])
valor2 = float(linha2[2])

valor_pago = numero1 * valor1 + numero2 * valor2

print("VALOR A PAGAR: R$", "{:.2f}".format(valor_pago))
