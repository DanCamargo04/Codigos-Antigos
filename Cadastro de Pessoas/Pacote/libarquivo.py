import Pacote.libfuncoes

def verificar_Arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"rt")
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_Arquivo(nomeArquivo):
    try:
        arq = open(nomeArquivo,"wt+")
        arq.close()
    except:
        print("Erro ao criar arquivo!")
    else:
        print("Arquivo {} criado com sucesso!".format(nomeArquivo))

def mostrar_Arquivo(nomeArquivo,msg = "Arquivo"):
    try:
        arq = open(nomeArquivo,"rt")
    except:
        print("Erro ao abrir o arquivo!")
    else:
        Pacote.libfuncoes.cabecalho(msg)
        for linha in arq:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print("\033[1;32m{} | {} anos\033[m".format(dado[0],dado[1]))

def cadastrar_Nova_Pessoa(nomeArquivo,nome = "desconhecido",idade = 0):
    try:
        arq = open(nomeArquivo,"at")
    except:
        print("Erro ao abrir o arquivo!")
    else:
        try:
            arq.write("Nome : {};Idade : {}\n".format(nome,idade))
        except:
            print("Erro ao cadastrar o/a {}".format(nome))
        else:
            print("{} cadastrado(a) com sucesso!".format(nome))

