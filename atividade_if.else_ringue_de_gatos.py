import random

poder_do_gato1 = random.randint(5, 10)
#nome: ronaldo

poder_do_gato2 = random.randint(5, 10)
#nome: alfredo

poder_do_gato3 = random.randint(5, 10)
#nome: carlos

gato_selecionado = input ("em qual gato você aposta 1, 2, 3? escreva e depois pressione enter para continuar -----> ")

if poder_do_gato1 > poder_do_gato2 :
    if poder_do_gato1 > poder_do_gato3 :
        if gato_selecionado == 1 :
           print ("você ganhou tome um pastel com uma coca gelada")
        else :
           print ("seu gato foi brutamente morto pelo gato 1 (ronaldo)") 
    else :
        if poder_do_gato1 == poder_do_gato3:
            print ("os gatos 1 e 3 empataram e viraram amigos (ronaldo e carlos)")
        else :
            if gato_selecionado == 3 :
                print ("você ganhou tome um pastel com uma coca gelada")
            else :
             print("seu gato foi brutalmente morto pelo gato 3 (carlos)")
else :
    if poder_do_gato1 == poder_do_gato2 :
        if poder_do_gato3 > poder_do_gato1 :
            print ("gato 1 e 2 viraram amigos até gato 3 brutalmente matar os dois (ronaldo, alfredo e carlos)")
        else :
            print ("os gatos 1 e 2 empataram e viraram amigos (ronaldo e alfredo)")
    else:
        if poder_do_gato2 > poder_do_gato3 :
            if gato_selecionado == 2 :
                print ("você ganhou tome um pastel com uma coca gelada")
            else :
                print("seu gato foi brutalmente morto pelo gato 2 (alfredo)")
        else :
            if poder_do_gato2 == poder_do_gato3 :
                print ("os gatos 3 e 2 empataram e viraram amigos (carlos e alfredo)")
            if gato_selecionado == 3 :
                print ("você ganhou tome um pastel com uma coca gelada")
            else :
                print("seu gato foi brutalmente morto pelo gato 3 (carlos)")

print ("o poder do gato 1 (ronaldo) era " + str(poder_do_gato1) )

print ("o poder do gato 2 (alfredo) era " + str(poder_do_gato2) )

print ("o poder do gato 3 (carlos) era " + str(poder_do_gato3) )

