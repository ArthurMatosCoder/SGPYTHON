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
            pet["fome"] -= random.randint(1,5)
            pet["felicidade"] -= random.randint(1,5)
            pet["energia"] -= random.randint(1,5)
        elif diminuir == 2:
            pet["fome"] -= random.randint(3,10)
            pet["felicidade"] -= random.randint(3,10)
            pet["energia"] -= random.randint(3,10)
        elif diminuir == 3:
            pet["fome"] -= random.randint(5,20)
            pet["felicidade"] -= random.randint(5,20)
            pet["energia"] -= random.randint(5,20)

pet = criar_pet()

while True:
    print("\n======================================================")

    oq_fazer = input(f"1.comer, 2.brincar, 3.dormir, 4.checar stats, 5.sair do jogo ---> ")
    if oq_fazer == "1" and personalidade_escolhida == "guloso":
        pet["fome"] += 20
        pet["felicidade"] += 20
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1":
        pet["fome"] += 20
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "1" and pet["fome"] > 80 :
        pet["fome"] += 20
        print(f"seu pet ta cheio")
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2" and personalidade_escolhida == "brincalhão":
        pet["felicidade"] += 35
        pet["energia"] -= 10
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "2":
        pet["felicidade"] += 20
        pet["energia"] -= 10
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "3" and personalidade_escolhida == "preguiçoso":
        time.sleep(5)
        pet["energia"] += 35
        pet["felicidade"] += 20
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "3":
        time.sleep(5)
        pet["felicidade"] += 20
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "4":
        print(pet)
        diminuir_stats(pet)
        limites(pet)
    elif oq_fazer == "5":
        print(f"foi legal o tempo que vc teve com seu pet, mas agora vc precisa viajar, vc o coloca para adoção e diz adeus, o vendo pela ultima vez")
        break
    else:
        print("opção invalida")


    if pet["fome"] <= 0:
        print("SEU PET MORREU DEFINHANDO NO CANTO ENQUANDO VC NÃO OLHAVA")
        break
    elif pet["felicidade"] <= 0:
        print("SEU PET DECIDE TE ABANDONAR ENQUANDO VC DORMIA")
        break
    elif pet["energia"] <= 0:
        print("SEU PET DESMAIA DO LADO DE FORA DA CASA ONDE SEU CORPO E DEVORADOS POR ANIMAIS SELVAGEIS")
        break

