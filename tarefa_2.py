import random
def gerar_numero():
    return random.randint(1,100)
numero = gerar_numero()
    def chutes():   
    tentativas = 0

    while True:
        chutes = (input("digite um numero "))
        if chutes > numero:
            tentativas += 1
            print("o numero e menor")
        elif chutes < numero:
            tentativas += 1
            print("o numero e maior")
        else:
            print("parabens voce acertou em", tentativas, "tentativas")
            print(gerar_numero())

            break



gerar_numero()
chutes()
