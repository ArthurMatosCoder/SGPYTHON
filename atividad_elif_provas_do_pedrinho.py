prova1 = int(input("qual a primeira nota? : "))

prova2 = int(input("qual a segunda nota? : "))

prova3 = int(input("qual a terceira nota? : "))

media = (prova1 + prova2 + prova3) / 3

print(f"sua media foi {media}")

if media < 5 :
    print ("ce foi um lixo mano")
elif media < 10 :
    print("ce foi aprovado :D")
else:
    print("CE E LOCO PERFCT")
