quadro = [["","",""],["","",""],["","",""]]

print("-"*18)
for i in range(0,3):
    for k in range(0,3):
        print(" {},{} ".format(i,k),end = " ")
    print("")
print("-"*18)

jogador = 1
simbolo = "X"

cont = 0

while cont < 9:
    cont += 1
    print("-=-"*5)
    print("\033[1;35mVez do jogador {}\033[m".format(jogador))
    print("-=-"*5)
    while True:
        xPos = int(input("Insira a 1° posição (X) : "))
        yPos = int(input("Insira a 2° posição (Y) : "))
        if (xPos >= 0 and xPos <= 2) and (yPos >= 0 and yPos <= 2):
            break
        else:
            print("\033[1;31mErro de valores! Tente novamente jogador {}\033[m".format(jogador))
            continue
    while quadro[xPos][yPos] == "X" or quadro[xPos][yPos] == "O":
        print("\033[1;31mErro! Já existe um simbolo nesse lugar!\033[m")
        print("Tente novamente jogador {}".format(jogador))
        xPos = int(input("Insira a 1° posição (X) : "))
        yPos = int(input("Insira a 2° posição (Y) : "))
    quadro[xPos][yPos] = simbolo
    print("Quadro atual : ")
    for c in quadro:
        print(c)
    if (quadro[0][0] == "X" and quadro[1][1] == "X" and quadro[2][2] == "X") or (quadro[0][2] == "X" and quadro[1][1] == "X" and quadro[2][0] == "X") or (quadro[0][0] == "X" and quadro[0][1] == "X" and quadro[0][2] == "X") or (quadro[1][0] == "X" and quadro[1][1] == "X" and quadro[1][2] == "X") or (quadro[2][0] == "X" and quadro[2][1] == "X" and quadro[2][2] == "X") or (quadro[0][0] == "X" and quadro[1][0] == "X" and quadro[2][0] == "X") or (quadro[0][1] == "X" and quadro[1][1] == "X" and quadro[2][1] == "X") or (quadro[0][2] == "X" and quadro[1][2] == "X" and quadro[2][2] == "X"):
        print("\033[1;33mJogador 1 é o vencedor!!!\033[m")
        break
    elif (quadro[0][0] == "O" and quadro[1][1] == "O" and quadro[2][2] == "O") or (quadro[0][2] == "O" and quadro[1][1] == "O" and quadro[2][0] == "O") or (quadro[0][0] == "O" and quadro[0][1] == "O" and quadro[0][2] == "O") or (quadro[1][0] == "O" and quadro[1][1] == "O" and quadro[1][2] == "O") or (quadro[2][0] == "O" and quadro[2][1] == "O" and quadro[2][2] == "O") or (quadro[0][0] == "O" and quadro[1][0] == "O" and quadro[2][0] == "O") or (quadro[0][1] == "O" and quadro[1][1] == "O" and quadro[2][1] == "O") or (quadro[0][2] == "O" and quadro[1][2] == "O" and quadro[2][2] == "O"):
        print("\033[1;32mJogador 2 é o vencedor!!!\033[m")
        break
    if jogador == 1:
        jogador = 2
        simbolo = "O"
    else:
        jogador = 1
        simbolo = "X"
print("FIM DO JOGO!")