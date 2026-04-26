import random

chuvendo = random.randint(1, 2)
# isso diz que esta chuvendo ou não, 1 igual a chuva e 2 igual a sem chuva

nublado = random.randint(1, 2)
# isso diz se esta nublado, 1 esta nublado 2 não esta nublado

if nublado == 1:
    if chuvendo == 1:
        print ("esta nublado e chuvendo leve seu guarda-chuva ")

    else:
        print("esta nublado mas não esta chuvendo leve o guarda-chuva")

if nublado == 2:
    if chuvendo == 1:
        print ("não esta nublado, mas, esta chuvendo leve seu guarda-chuva ")

    else:
        print("não esta nublado e não esta chuvendo pode ir sem o guarda-chuva")
