#Exercicio 3.15

cigarros_dia = int(input("quantidade de cigarros fumados por dia: "))
anos = int(input("há quanto tempo é fumante (em anos): "))

anos_em_dias = anos * 365

perda_dia = 1/6 * 1/24* cigarros_dia
perda_anos = perda_dia * anos_em_dias

print("O total de dias de vida perdido é:", perda_anos)
   


    


