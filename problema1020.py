#Problema 1019 - BeeCrowd - Conversão de Tempo

idade = int(input())

anos = idade//365
print("{} ano(s)".format(anos))
resto_anos = idade % 365

meses = resto_anos//30
print("{} mes(es)".format(meses))
resto_meses = resto_anos%30
      
dias = resto_meses
print("{} dia(s)".format(dias))

