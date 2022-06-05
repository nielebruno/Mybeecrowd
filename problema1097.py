#Problema 1097 - Sequência IJ3

jotas = [1,2,3]

#com problema nao funciona por causa da precisão numerica do float (ao incrementar 0.2 existe um erro de aproximação acumulativo que ao chegar no 1.8 + 0.2 não dá 2
I = 0
while I <= 2:
    for i in range(3):
        #jotas[i] = jotas[i]+0.2
        J = jotas[i]+I
        if (I == int(I)):
            print("I={} J={}".format(int(I),int(J)))
        else:
            print("I={:.1f} J={:.1f}".format(I,J))
        #jotas[i] = jotas[i]+0.2
    I = I + 0.2

'''#com problema nao funciona por causa da precisão numerica do float (ao incrementar 0.2 existe um erro de aproximação acumulativo que ao chegar no 1.8 + 0.2 não dá 2
I = 0
while I <= 2:
    for i in range(3):
        #jotas[i] = jotas[i]+0.2
        J = jotas[i]+I
        if (I == int(I)):
            print("I={} J={}".format(int(I),int(J)))
        else:
            print("I={:.1f} J={:.1f}".format(I,J))
    I = round(I + 0.2,1)
'''
