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







frutas = ["uva", "banana", "maçã"]
numero = [10, 20, 15, 45, 5]
frutas.append("maracuja")
numero.remove(20)
frutas.remove("banana")
frutas.remove(frutas[0])
naoquero = frutas.pop(1)
frutas.insert(0, 50)
del frutas[1]
for fruta in frutas:
    print(fruta)
    print(numero)

numero.sort()
print(numero)
frutas.sort()
print(frutas)
numero.reverse()
print(numero)
frutas.reverse()
print(frutas)










pessoa = {
    'nome': 'ana',
    'idade': 30,
    'cidade': 'fortaleza',
    'cidade': 'fortaleza'}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])
print(pessoa)


































usuario = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "Santos",
    "profissão": "professor"
}

for vaca, boi in usuario.items():
    print(vaca, boi)













quadrados = [x ** 2 for x in range(5)]
print(quadrados)














