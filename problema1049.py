#Problema 1049 - Beecrowd - Animal

vertebra = input()
tipo = input()
comida = input()
animal = str()

if vertebra == "vertebrado":
    if tipo == "ave":
        if comida == "carnivoro":
            animal = "aguia"
        elif comida == "onivoro":
            animal = "pomba"
    elif tipo == "mamifero":
        if comida == "onivoro":
            animal = "homem"
        elif comida == "herbivoro":
            animal = "vaca"
elif vertebra == "invertebrado":
    if tipo == "inseto":
        if comida == "hematofago":
            animal = "pulga"
        elif comida == "herbivoro":
            animal = "lagarta"
    elif tipo == "anelideo":
            if comida == "hematofago":
                animal = "sanguessuga"
            elif comida == "onivoro":
                animal = "minhoca"

print("{}".format(animal))
