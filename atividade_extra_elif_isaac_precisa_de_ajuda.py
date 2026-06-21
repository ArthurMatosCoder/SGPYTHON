print("o isaac vai lutar contra a mãe defina os estatos dele")

biblia = input("você tem a biblia? ")

carregada = input("sua biblia esta carregada? ")

brimstone = input("você tem uma brindstone? ")

skill = input("você é noob, bom ou pro? ")

if biblia == "sim" and carregada == "sim" :
    print ("você deu hitkill com a biblia")
elif skill == "pro" and brimstone == "sim" :
    print ("moleza")
elif (skill == "pro" and brimstone == "não") or (skill == "bom" and brimstone == "sim") :
    print("foi chatinho, mas deu certo")
elif (skill == "noob") or (skill == "bom" and brimstone == "não") :
    print ("você morreu")
