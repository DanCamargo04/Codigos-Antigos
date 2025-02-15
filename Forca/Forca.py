palavra = str(input("Insira a palavra : "))
listaLetras = list()
listaCodificada = list()
erros = 0
cont = 0
for c in palavra:
    listaLetras.append(c)
    listaCodificada.append("*")
digitados = list()
while erros < 12:
    cont += 1
    print("{}\nPalavra : {}\n{}".format("-"*20,"".join(listaCodificada),"-"*20))
    tentativa = str(input("Insira sua tentativa : "))
    if tentativa in digitados:
        print("Você ja digitou essa letra!")
    elif len(tentativa) > 1:
        print("Insira uma letra e não uma palavra!")
    else:
        for i,c in enumerate(listaLetras):
            if tentativa in listaLetras:
                if c == tentativa:
                    listaCodificada[i] = tentativa
                    digitados.append(tentativa)
            elif tentativa not in listaLetras:
                print("\033[1;31mErrou!\033[m")
                erros += 1
                digitados.append(tentativa)
                break
    if "*" not in listaCodificada:
        print("\033[1;32mVocê venceu!!!\033[m")
        break
print("\033[1;33mA palavra era {}\033[m".format(palavra))
print("\033[1;33mVocê levou {} tentativas para tentar acertar\033[m".format(cont))