#Módulo para a construção do programa princial

def linha(tamanho = 40):
    print("-"*tamanho)

def cabecalho(msg,tamanhoLinha = 40):
    linha()
    print(msg.center(tamanhoLinha))
    linha()

def menu(lista):
    linha()
    menuPhrase = "MENU"
    print(" "*16 + menuPhrase)
    linha()
    for i,c in enumerate(lista):
        print(" \033[1;33m{}\033[m -> \033[1;34m{}\033[m".format(i+1,c))
    linha()

def leiaInt(msg):
    try:
        n = int(input(msg))
    except (ValueError,TypeError):
        print("\033[1;31mTipo de dado ou valor incorreto!\033[m")
    else:
        return n