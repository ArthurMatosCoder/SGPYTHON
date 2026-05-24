prova1 = float(input("qual a primeira nota? : "))

prova2 = float(input("qual a segunda nota? : "))

prova3 = float(input("qual a terceira nota? : "))

media = (prova1 + prova2 + prova3) / 3

print(f"sua media foi {media}")

if media <= 4.999 :
    print ("CE FOI UM LIXO E REPROVOU COM UM F")
elif media <= 5.999 :
    print ("ce foi um lixo mano tirou um F mas não reprovou MELHORE")
elif media < 10 :
    if media <= 6.999 :
        print("ce foi aprovado com um D")
    elif media <= 7.999 :
        print("ce foi aprovado com um C")
    elif media <= 8.999 :
        print("ce foi aprovado com um B")
    elif media < 10 :
        print("ce foi aprovado com um A")
else:
    print("CE E LOCO PERFCT com um A")
