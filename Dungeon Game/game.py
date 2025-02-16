from random import randint
numeroSala = 1
escolhaCaminho = 0
cont = 0
print("\nOlá aventureiro! :D\n")
print("--------------------------\n\033[1;33mSala atual (inicial) : {}\033[m\n--------------------------".format(numeroSala))
while numeroSala != 9 and cont < 7:
    escolhaCaminho = int(input("Qual caminho você seguirá ?\n[1] \033[1;31mVermelho\033[m\n[2] \033[1;37mPreto\033[m\nEscolha : "))
    if(numeroSala == 8 and escolhaCaminho == 2):
        print("\n\033[1;35m* Você caiu na dungeon dos controladores do espaço-tempo! Teleportando para uma sala aleatória ... *\033[m\n")
        numeroSala = randint(1,5)
    elif(numeroSala == 6):
        numeroSala += 2
        print("\n\033[1;34m* Não fez diferença o que você digitou! Da sala 6 foi enviado automaticamente para a sala 8! *\033[m\n")
    elif(escolhaCaminho == 1 or escolhaCaminho == 2):
        numeroSala += escolhaCaminho
    else:
        print("\033[1;31mNumero inválido!\033[m")
    print("----------------------\n\033[1;33mSua sala atual é : {}\033[m\n----------------------\n".format(numeroSala))
    cont = cont + 1
if(numeroSala == 9):
    print("\033[1;32mVocê venceu! Parabens por chegar na sala 9 !!!\033[m\n")
elif(cont >= 7):
    print("\033[1;31mVocê perdeu por excesso de jogadas!\033[m\n")
print("Total de jogadas : {}\n".format(cont))
