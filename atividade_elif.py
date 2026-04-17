IDADE=int(input("digide sua idade: " ))
ingresso_comprado = input("se tive comprada digite sim: ")
autorizacao=input("se tiver autorizacao dos pais digite sim")
lista_vip= input ("ser tiver na lista digiti sim ")

if idade < 12:
    print("nao pode entrar")

elif idade>=18 and ( imgresso_comprado == "sim" or lista_vip=="sim"):
    print ("pode entrar ")

elif idade < 18 and (imgresso_comprado == "sim" or lista_vip=="sim") and autorizacao == "sim" :
    print ("pode entrar ")

else:
    print("entrada negada" )
