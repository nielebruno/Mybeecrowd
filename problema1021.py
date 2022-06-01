#Problema 1021 - Beecrowd

import math

N = float(input())
nota = math.floor(N)
decimal = N - nota
moedas = decimal * 100

if (N >= 0) and (N <= 1000000.00):
    #Notas R$ 100,00
    print("NOTAS:")
    N100 = nota//100
    print("{} nota(s) de R$ 100.00".format(N100))
    
    #Notas R$ 50,00
    nota50 = nota%100
    N50 = nota50//50
    print("{} nota(s) de R$ 50.00".format(N50))

    #Notas R$ 20,00
    nota20 = nota50%50
    N20 = nota20//20
    print("{} nota(s) de R$ 20.00".format(N20))

    #Notas R$ 10,00
    nota10 = nota20%20
    N10 = nota10//10
    print("{} nota(s) de R$ 10.00".format(N10))

    #Notas R$ 5,00
    nota5 = nota10%10
    N5 = nota5//5
    print("{} nota(s) de R$ 5.00".format(N5))

    nota2 = nota5%5
    N2 = nota2//2
    print("{} nota(s) de R$ 2.00".format(N2))
    
    print("MOEDAS:")
    #Moedas R$ 1,00
    moeda1 = nota2%2
    N1 = moeda1
    print("{} moeda(s) de R$ 1.00".format(N1))

    
    #Moedas R$ 0,50
    m50c = int(moedas//50)
    print("{} moeda(s) de R$ 0.50".format(m50c))

    #Moedas R$ 0,50
    moedas25=moedas%50
    m25c = int(moedas25//25)
    print("{} moeda(s) de R$ 0.25".format(m25c))


    #Moedas R$ 0,10
    moedas10c = moedas25%25
    m10c = int(moedas10c//10)
    print("{} moeda(s) de R$ 0.10".format(m10c))

    #Moedas R$ 0,05
    moedas5c = moedas10c%10
    m5c = int(moedas5c//5)
    print("{} moeda(s) de R$ 0.05".format(m5c))

    #Moedas R$ 0,01
    moedas1c = moedas5c%5
    m1c = int(moedas1c//1)
    print("{} moeda(s) de R$ 0.01".format(m1c))
