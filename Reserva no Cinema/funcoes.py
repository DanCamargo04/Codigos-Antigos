# Módulo

from random import randint

def create_head(title = "head_name",hasDetail = False,lineSize = 60):
    if hasDetail == False:
        print("-"*lineSize)
        print(title.center(lineSize))
        print("-"*lineSize) 
    else:
        print("-=-"*20)
        print(title.center(60))
        print("-=-"*20)


def create_menu(optionsList:list, title = "menu_name", lineSize = 60):
    print("-"*lineSize)
    print("\033[1;34m{}\033[m".format(title.center(lineSize)))
    print("-"*lineSize)
    for i,c in enumerate(optionsList):
        print("\033[1;36m{}\033[m - \033[1m{}\033[m".format(i+1,c))
    print("-"*lineSize)


def book_seats(reservationsList:list, personFullName:str, movieDigit:int, amountSeats:int,moviesList:list):
    auxList = []
    verCont = 0
    verMovie = 0
    data = {"name":"","movie":0,"seats":[],"code":0}
    for i in range(amountSeats):
        try:
            number = int(input("Insira o número da {}° cadeira : ".format(i+1)))
        except:
            print("\033[1;31mEsse tipo de dado está incorreto!\033[m")        
        else:
            auxList.append(number)
            for i,c in enumerate(reservationsList):
                if c["movie"] == movieDigit and number in c["seats"]:
                    verCont = 1
                    break
    if verCont == 0:
        while True:
            code = randint(100000,999999)
            isValid = False
            for i,c in enumerate(reservationsList):
                if c["code"] == code:
                    isValid = False
                    break
                elif i == len(reservationsList)-1:
                    isValid = True
            if isValid == True:
                break
        data = {"name":personFullName,"movie":movieDigit,"seats":auxList,"code":code}
        reservationsList.append(data.copy())
        create_head("        \033[1;32mSucesso!\033[m")
        print("\033[1;32mReserva criada!\033[m")
        print("Nome(responsável) : {}".format(data["name"]))
        print("Filme : {}".format(moviesList[movieDigit-1]))
        print("Assento(s) : ",end = "")
        for i,c in enumerate(data["seats"]):
            if i == len(data["seats"])-1:
                print(c)
            else:
                print(c,end = " ")
        print("Código de entrada : {}".format(data["code"]))
        print("-"*60)
        data.clear()
    else:
        create_head("        \033[1;31mErro\033[m")
        print("\033[1;31mErro ao realizar cadastro! Este assento já esta ocupado!\033[m")
        print("-"*60)


def show_reservation_data(reservationsList:list,code:int,movieChoice:int,movieList:list):
    for i,c in enumerate(reservationsList):
        if c["code"] == code:
            create_head("        \033[1;34mDados da reserva\033[m")
            print("Nome(responsável) : {}".format(c["name"]))
            print("Filme : {}".format(movieList[movieChoice]))
            print("Assento(s) : ",end = "")
            for j in c["seats"]:
                print(j,end = " ")
            print()
            print("-"*60)
            break
        elif i == len(reservationsList)-1:
            print("\033[1;31mNão foi encontrada nenhuma reserva com esse código!\033[m")


def delete_reservation(reservationsList:list,code:int):
    for i,c in enumerate(reservationsList):
        if c["code"] == code:
            try:
                reservationsList.pop(i)
            except:
                print("\033[1;31mErro ao remover reserva da lista!\033[m")
            else:
                print("\033[1;32mReserva de numero {} cancelada com sucesso!\033[m".format(code))
                break
        elif i == len(reservationsList)-1:
            print("\033[1;31mNão foi encontrada nenhuma reserva com esse código!\033[m")


