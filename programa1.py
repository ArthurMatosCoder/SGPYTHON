jogos = {
    "minecraft":"jogo 1",
    "resident evil":"jogo 2",
    "dragon ball":"jogo 3"
}
while True:
    print("\n===MENU===")
    print("1 - ver jogos")
    print("2 - inserir jogos")
    print("3 - sair")

    opcao = input ("escolha: ")
   #ver jogos
    if opcao == "1":
        print("\n===JOGOS===")

        nomes = list(jogos.keys())

        for i, nome in enumerate(nomes,1):
            print(f"{i} - {nome}")
        print("0 - voltar")
        escolha = input ("escolha um jogo: ")
        if escolha == "0":
            continue
        if escolha.isdigit() and 1 <= int(escolha) <= len(nomes):
            nomes = nomes[int(escolha) - 1]
            while True:
                print(f"\n ==={nomes}===")
                print("1 - para ver sinopse")
                print("2 - voltar")
                opcao_jogo = input ("escolha: ")
                if opcao_jogo == "1":
                    print("\n SINOPSE: ")
                    print(jogos[nomes])
                elif opcao_jogo == "2":
                    break
                else:
                    print("Opção errada")
    elif opcao == "2":
        nome = input("qual o nome do jogo? ")
        sinopse = input("descrisção do jogo: ")
        jogos[nome] = sinopse
        print("jogo adicionado com sucesso")
    elif opcao == "3":
        print("saindo")
        break
