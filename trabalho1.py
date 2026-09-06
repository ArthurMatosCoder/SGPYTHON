palavra = input("Digite uma palavra: ").lower()
letras_descobertas = ["_"] * len(palavra)
vida = 8
while vida > 0:
    print(letras_descobertas)
    chute = input("Digite uma letra: ").lower()

    for letra in chute:
        if letra == palavra:
            print(palavra, end=" ")
            for palavra in letras_descobertas:
                letras_descobertas[i]       
        else:
            print("_", end=" ")
            print("\nPalavra:", "".join(letras_descobertas))
