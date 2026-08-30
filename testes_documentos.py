idade = 15
documento = True

if idade >= 18 and documento == True :
    print("entrada autorizada")
elif idade >= 18 and documento == False :
    print("documento necessário")
else:
    print("idade invalida")
