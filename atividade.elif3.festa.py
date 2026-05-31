idade = int(input("qual a idade? " ))

vip = input("e vip? " )

pais = input("tem autorizacão dos pais? " )

ingresso = input("tem ingresso? " )

if (( idade >= 18 and (ingresso or vip == "sim") ) or (idade < 18 and idade > 12 and pais == "sim" and (ingresso or vip == "sim") ) ):
    print("você pode entrar na festa")
else :
    print("você não pode entrar")
