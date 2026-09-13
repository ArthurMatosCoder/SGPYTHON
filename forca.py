palavras = input("digite uma palavra: ")
letras_descobertas = ["_"] * len(palavras)
vidas = 8
while vidas > 0 and "_" in letras_descobertas:
    print("\nPalavras:", " ".join(letras_descobertas))
    print("tentativas restantes: ", vidas)
    chute = input("de um chute: ").lower()

    if chute in palavras:
        for i in range(len(palavras)):
            if palavras[i] == chute:
                letras_descobertas[i] = chute
        print("acertou meu mano")
    else:
        vidas -= 1
        print("errou otario")

if "_" not in letras_descobertas:
    print("chutador ganhou ",palavras)
else:
    print("criador da palavra ganhou")
    print("a palavra era ", palavras)
