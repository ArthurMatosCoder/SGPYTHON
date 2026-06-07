idade = int(input("qual sua idade? "))

tem_experiencia = input("tem experiencia? ")

crimes = input("cometeu crimes? ")

ensino = input("completou a facudade? ")

indicado = input("voce foi indicado por alguem da empressa? ")

if idade > 18 and tem_experiencia == "sim" and crimes == "não" :

    print("voce foi contratado")

elif tem_experiencia == "não" and (ensino == "sim" or indicado == "sim")  and crimes == "não" :

    print("voce foi para entrevista")

else:
    print("mais sorte da proxima vez")
