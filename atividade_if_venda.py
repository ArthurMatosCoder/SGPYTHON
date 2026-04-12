import random

preço = float(f"{random.uniform (1.0 , 10.0):.2f}")

print ("Vendedor: OLHA O JOGO OLHA O JOGO SO " + str(preço) + " REAIS") 

carteira = float(f"{random.uniform (0.0 , 50.0):.2f}")

quantidade = random.randint (1 , 4)

print("criança: oi eu quero comprar esse sonico e outros " + str(quantidade) + " mas so tenho " + str(carteira) + " reais, vai dar para comprar?")

quantidade += 1

if carteira < preço * quantidade:
    print(f"vendedor: vai dar não amiguinho, tão faltando {(preço * quantidade - carteira):.2f} reais" )

if carteira > preço * quantidade:
    carteira -= preço * quantidade
    print(f"vendedor: da sim! e sobra { carteira :.2f} reais")
