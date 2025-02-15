#----------------------------------------------------------------------------------------------------------
# 1-Criar um sistema de reserva de assento em uma sala de cinema para um filme específico.
# 2-INPUT(Cadastrar o nome completo de apenas uma pessoa, inserir o filme e os assentos.)
# 3-OUTPUT(Mostrar se foi concluída a reserva com sucesso, o número da sala e um código caso necessário.)
# 4-Caso já tenha assento ocupado ou não exista, e ou o filme não exista tambem, mostrar uma mensagem de erro.
# 5-Opções para mostrar as reservas feitas pelo código adquirido.
# 6-Colorir terminal para deixar mais agradável.
# 7-KEYS utilizadas no dicionario : 'name', 'movie', 'seats' e 'code'.
# 8-Existe um easter egg, boa sorte em tentar achá-lo!
#----------------------------------------------------------------------------------------------------------
# TO-DO
# Nada no momento.
#-----------------------------------------------------------------------------------------------------------

from funcoes import *
from time import sleep

def main():
    susCont = 0
    create_head("        \033[1;35mBem vindo ao cinema!\033[m",True)
    moviesList = ["Batman","Velozes e Furiosos","Toy Story 4","Os incríveis","Gente Grande 2"]
    reservationList = [{"name":"Lucas Gabrielison","movie":2,"seats":[10,11,12],"code":123345}]
    optionList = ["Reserva de assentos","Exibir reserva","Cancelar reserva","Sair do sistema","\033[1;33mSou funcionário\033[m"]
    employeeOptionsList = ["Adicionar novo filme no cartaz","Remover um filme do cartaz","Ver todos os responsáveis de reservas","Sair para parte de usuários (voltar)"]
    password = 6543123

    while True:
        create_menu(optionList,"Opções")
        movieDigit = 0
        try:
            option = int(input("Insira sua opção : "))
        except:
            print("\033[1;31mDado inserido está incorreto (tipo ou valor)!\033[m")
        else:
            if option == 1:
                fullName = str(input("Insira seu nome completo : ")).strip().title()
                print("-"*60)
                for i,c in enumerate(moviesList):
                    print("\033[1;36m{}\033[m - \033[1m{}\033[m".format(i+1,c))
                print("-"*60)
                movieDigit = int(input("Insira numero do filme : "))
                if movieDigit <= 0 or movieDigit > len(moviesList):
                    print("\033[1;31mOpção de filme incorreta!\033[m")
                else:
                    amountSeats = int(input("Insira a quantidade de assentos : "))
                    book_seats(reservationList,fullName,movieDigit,amountSeats,moviesList)
            elif option == 2:
                movieChoice = 0
                showCode = int(input("Insira o código de entrada para verificar seus dados : "))
                for i,c in enumerate(reservationList):
                    if c["code"] == showCode:
                        movieChoice = c["movie"]
                show_reservation_data(reservationList,showCode,movieChoice-1,moviesList)
            elif option == 3:
                secureAnswer = str(input("\033[1;33mVocê tem certeza de que quer deletar sua reserva? [S/N] : \033[m")).strip().upper()
                if secureAnswer == "S" or secureAnswer == "SIM" or secureAnswer == "SS" or secureAnswer == "SE" or secureAnswer == "YES" or secureAnswer == "YEAH" or secureAnswer == "YEA":
                    deletionCode = int(input("Insira o seu código de entrada : "))
                    delete_reservation(reservationList,deletionCode)
                else:
                    print("\033[1;33mRetornando ao menu...\033[m")
            elif option == 4:
                print("\033[1;33mSaindo do sistema...\033[m")
                break
            elif option == 5:
                employeePassword = int(input("Insira a senha dos funcionários : "))
                if employeePassword == password:
                    while True:
                        create_menu(employeeOptionsList,"Bem vindo(a) funcionário(a)!")
                        employeeOption = int(input("Insira sua opção : "))
                        if employeeOption == 1:
                            newMovieName = str(input("Insira o nome do filme a ser adicionado no cartaz : "))
                            if newMovieName not in moviesList:
                                moviesList.append(newMovieName)
                                print("\033[1;32mSucesso! Filme adicionado ao cartaz!\033[m")
                            else:
                                print("\033[1;31mErro! Filme já existe no cartaz!\033[m")
                        elif employeeOption == 2:
                            print("-"*60)
                            for i,c in enumerate(moviesList):
                                print("\033[1;36m{}\033[m - \033[1m{}\033[m".format(i+1,c))
                            print("-"*60)
                            try:
                                removalOption = int(input("Insira o numero do filme a ser removido : "))
                            except:
                                print("\033[1;31mErro! Valor incorreto e/ou desconhecido!\033[m")
                            else:
                                if removalOption > 0 and removalOption <= len(moviesList):
                                    moviesList.pop(removalOption-1)
                                    print("\033[1;32mSucesso! Filme retirado do cartaz!\033[m")
                                else:
                                    print("\033[1;31mErro! Opção inválida!\033[m")
                        elif employeeOption == 3:
                            print()
                            print("\033[1mResponsáveis registrados ({}) : \033[m".format(len(reservationList)))
                            for i,c in enumerate(reservationList):
                                print("{} - {}".format(i+1,c["name"]))
                            print()
                        elif employeeOption == 4:
                            print("\033[1;33mSaindo da parte de funcionários...\033[m")
                            break     
                        else:
                            print("\033[1;31mOpção inválida!\033[m")               
                else:
                    print("\033[1;31mSenha inválida!\033[m")
            elif option == 666:
                create_head("SUS")
                print("ඞ "*30)
                print("-"*60)
                if susCont == 0:
                    print("     \033[1;35mBom trabalho! Tu acabou de achar o easter egg!\033[m".center(60))
                    print("-"*60)
                susCont += 1
                sleep(2)
            else:
                print("\033[1;31mOpção inválida!\033[m")
            sleep(0.75)


if __name__ == "__main__":
    main()
