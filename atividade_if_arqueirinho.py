import random

flechas = random.randint(10 , 50)
#o numero de flechas

print ( "voce tinha " + str(flechas) + " flechas no inicio")

ondas = 1
#qual onda voce esta

inimigos_por_onda = 10

while flechas > inimigos_por_onda:

    flechas -= inimigos_por_onda

    ondas += 1

    flechas += flechas / 2

    inimigos_por_onda += inimigos_por_onda / 2


print ("voce perdeu na onda " + str(ondas) + " e tinha " + str(inimigos_por_onda)+ " inimigos na onda e sobraram " + str(inimigos_por_onda - flechas) + " vivos")

if ondas == 1:
    print("seu rank: PESSIMO")
    
if ondas == 2:
    print("seu rank: RUIM ")

if ondas == 3:
    print("seu rank: MAIS OU MENOS")

if ondas == 4:
    print("seu rank: BOM")


if ondas == 5:
    print("seu rank: PERFEITO")
