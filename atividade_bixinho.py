import random
import time

personalidades = [
    "brincalhão",
    "guloso",
    "timido",
    "preguiçoso",
]    

personalidade_escolhida = random.choice(personalidades)
def criar_pet():
    if personalidade_escolhida == "timido":
        texto_da_personalidade = "ve e se esconde enquando te encara com medo nos olhos"
    elif personalidade_escolhida == "guloso":
        texto_da_personalidade = "ve e oferece uma fruta"
    elif personalidade_escolhida == "preguiçoso":
        texto_da_personalidade = "ve e dorme e dorme no seu colo"
    elif personalidade_escolhida == "brincalhão":
        texto_da_personalidade = "ve corre até suas pernas e fica pedindo carinho se esfregando em você"

    nome_do_pet = input("Nome do pet: ")
    print(f"O {nome_do_pet} te {texto_da_personalidade}!")

    pet = {
        "nome": nome_do_pet,
        "personalidade" : personalidade_escolhida,
        "fome" : 100,
        "energia" : 100,
        "felicidade" : 100
    }
    return pet

def limites(pet):
    for atributo in pet:
        if atributo in ("fome", "energia", "felicidade"):
            pet[atributo] = max(0, min(100, pet[atributo]))

def diminuir_stats(pet):
        diminuir = random.randint(1,4)
        if diminuir == 1:
            pet["fome"] -= 1
            diminuir_stats(pet)
        elif diminuir == 2:
            pet["felicidade"] -= 1
            diminuir_stats(pet)
        elif diminuir == 3:
            pet["energia"] -= 1
            diminuir_stats(pet)





meu_pet = criar_pet()
