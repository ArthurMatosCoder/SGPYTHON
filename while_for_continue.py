c = 0
while c < 5:
    for numero in range(10):
        if numero == 5:
            print(numero)
    c += 1









for numero in range(5):
    if numero == 2:
        continue
    print(numero)






frutas = ["maçã", "banana", "uva"]
frutas.append("maracuja")
frutas.remove(frutas[0])
naoquero = frutas.pop(1)
frutas.insert(0, 50)
del frutas[1]
for fruta in frutas:
    print(fruta)

custo = frutas[0] + 50
print(custo)
