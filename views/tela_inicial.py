def tela_inicial():
    controlador = 0
    print("Meu Menu")

    while(controlador!=3):
        controlador = int(input("Digite 3 para deslogar"))

        if controlador == 3:
            print("Deslogado")
            break
        else:
            print("Sistema rodando")