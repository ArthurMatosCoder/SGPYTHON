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
        "felicidade" : 100,
        "carinho" : 100
    }
    return pet


def limites(pet):
    for atributo in pet:
        if atributo in ("fome", "energia", "felicidade", "carinho"):
            pet[atributo] = max(0, min(100, pet[atributo]))

import random
def evento(pet):
    if random.random() < 0.30:
        eventos = [
            "pediu carinho",
            "brincou sozinho",
            "quebrou um brinquedo"
        ]
        if random.choice(eventos) == "pediu carinho":
            quer_carinho = 1
            print(pet["nome"], "quer carinho")
        elif random.choice(eventos) == "brincou sozinho":
            pet["felicidade"] += 35
            pet["energia"] -= 10
            print(pet["nome"], "brincou sozinho")
        elif random.choice(eventos) == "quebrou um brinquedo":
            pet["felicidade"] -= 20
            pet["carinho"] -= 20
def diminuir_stats(pet):
        diminuir = random.randint(1,4)
        if diminuir == 1:
            pet["fome"] -= random.randint(1,5)
            pet["felicidade"] -= random.randint(1,5)
            pet["energia"] -= random.randint(1,5)
            pet["carinho"] -= random.randint(1, 5)
        elif diminuir == 2:
            pet["fome"] -= random.randint(3,10)
            pet["felicidade"] -= random.randint(3,10)
            pet["energia"] -= random.randint(3,10)
            pet["carinho"] -= random.randint(3, 10)
        elif diminuir == 3:
            pet["fome"] -= random.randint(5,20)
            pet["felicidade"] -= random.randint(5,20)
            pet["energia"] -= random.randint(5,20)
            pet["carinho"] -= random.randint(5, 20)
pet = criar_pet()

while True:
    print("\n======================================================")

    oq_fazer = input(f"1.comer, 2.brincar, 3.dormir, 4.dar carinho, 5.checar stats, 6.sair do jogo ---> ")
    if oq_fazer == "1" and personalidade_escolhida == "guloso" and pet["fome"] > 80 and pet["carinho"] == 0:
        pet["fome"] += 20
        print(pet["nome"], " corre até sua tijela de comida e devora tudo, mas ele parece estar chorando e cheio")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1" and personalidade_escolhida == "guloso" and pet["fome"] > 80:
        pet["fome"] += 20
        print(pet["nome"], " corre até sua tijela de comida e devora tudo, parece cheio")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1" and personalidade_escolhida == "guloso" and pet["carinho"] == 0:
        pet["fome"] += 20
        print(pet["nome"], " corre até sua tijela de comida e devora tudo, mas ele parece triste")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1" and personalidade_escolhida == "guloso":
        pet["fome"] += 20
        pet["felicidade"] += 20
        print(pet["nome"], " corre até sua tijela de comida e devora tudo")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1" and pet["fome"] > 80:
        pet["fome"] += 20
        print(pet["nome"], " chega a tijela e come tudo, e fica de buxin cheio")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1":
        pet["fome"] += 20
        print(pet["nome"], " chega a tijela e come tudo")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2" and pet["energia"] < 35:
        print(pet["nome"], "não quer brincar com você")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2" and personalidade_escolhida == "brincalhão" and pet["carinho"] == 0:
        pet["energia"] -= 10
        print(pet["nome"], " brinca com você meio sem vontade ele parece não se divertir")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2" and personalidade_escolhida == "brincalhão":
        pet["felicidade"] += 35
        pet["energia"] -= 10
        print(pet["nome"], " brinca com você com muita energia e felicidade")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2" and pet["carinho"] == 0:
        pet["energia"] -= 10
        print(pet["nome"], " brinca com você sem nenhuma vontade ele parece não se divertir")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2":
        pet["felicidade"] += 20
        pet["energia"] -= 10
        print(pet["nome"], " brinca com você, ficando bem animado")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "3" and personalidade_escolhida == "preguiçoso" and pet["carinho"] == 0:
        time.sleep(5)
        pet["energia"] += 35
        print("você coloca ", pet["nome"], " para dormir ele adormeçe rapido, mas parece ter pesadelos")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "3" and personalidade_escolhida == "preguiçoso":
        time.sleep(5)
        pet["energia"] += 35
        pet["felicidade"] += 20
        print("você coloca ", pet["nome"], " para dormir ele adormeçe rapido, ele parece adorar")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "3":
        time.sleep(5)
        pet["energia"] += 35
        print("você coloca ", pet["nome"], " para dormir")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "4" and personalidade_escolhida == "timido":
        pet["felicidade"] += 20
        pet["carinho"] += 40
        print("você da carinho no ", pet["nome"], " ele parece adorar")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "4":
        pet["felicidade"] += 20
        pet["carinho"] += 20
        print("você da carinho no ", pet["nome"], " ele parece gostar")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "5":
        print(pet)
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "6":
        print(f"foi legal o tempo que vc teve com seu pet, mas agora vc precisa viajar, vc o coloca para adoção e diz adeus, o vendo pela ultima vez")
        break
    else:
        print("opção invalida")

    evento(pet)
    
    if pet["fome"] <= 0:
        print("SEU PET MORREU DEFINHANDO NO CANTO ENQUANDO VC NÃO OLHAVA")
        break
    elif pet["felicidade"] <= 0:
        print("SEU PET DECIDE TE ABANDONAR ENQUANDO VC DORMIA")
        break
    elif pet["energia"] <= 0:
        print("SEU PET DESMAIA DO LADO DE FORA DA CASA ONDE SEU CORPO E DEVORADOS POR ANIMAIS SELVAGEIS")
        break
