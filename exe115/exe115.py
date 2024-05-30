# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções
# cadastrar uma nova pessoa
# listar todas as pessoas cadastradas
from os import system



def msg(msg, linha_cima=1, linha_baixo=1, pattern='-'):
    '''
    msg mostra a mensagem
    pattern='-' vem ante e depois da mensagem
    '''
#    tot = len(msg) + 50
    tot = 50
    if linha_cima== 1:
        print(f'{pattern}' * tot)
    print(f'{msg: ^{tot}}')
    if linha_baixo == 1:
        print(f'{pattern}' * tot)


def opcoes():

    print('''
\033[1;33m1\033[m - \033[1;34m Ver pessoas cadastradas \033[m
\033[1;33m2\033[m - \033[1;34m Cadastrar nova Pessoa   \033[m
\033[1;33m3\033[m - \033[1;34m Limpar Tela              \033[m
\033[1;33m4\033[m - \033[1;34m Sair do SISTEMA         \033[m

''')


def cadastrar_dados():
    nome = input('Nome: ').strip().lower()
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            print('Entre com um valor inteiro para idade!')

    try:
        usuarios = open('dados.txt', 'a')
        usuarios.write(f'{nome: <20} {idade}\n')
        usuarios.close()
    except ValueError as erro:
        print(f'O erro foi: {erro}')
   
    # cadastrar uma nova pessoa e salvar em um arquivo
    # criar uma função para cadastrar
    # se o arquivo não existir criar uma arquivo
    # se o arquivo existir addicionar as novas informações no final do arquivo


def mostrar_dados():
    try:
        print('-' * 40)
        usuarios = open('dados.txt', 'r')
        print(usuarios.read())
        usuarios.close()
        print('-' * 40)
    except:
        msg('O arquivo dados.txt não existe', 1, 1, '*')
    # mostrar o conteúdo de arquivo onde estão as pessoas cadastradas
    # criar uma função para mostrar 


def escolha():
    try:
        resp = int(input('\033[1;35mSua Opção: \033[m'))
    except:
        resp = 0
        print(f'\033[1;31mERRO! Digite uma opção valida [ 1 | 2 | 3 ]\033[m')
        while resp not in (1,2,3,4):
            try:
                resp = int(input('\033[1;35mSua Opção: \033[m'))
                break
            except ValueError as eRRo:
                print(f'\033[1;31mERRO! Digite uma opção valida [ 1 | 2 | 3 ]\033[m')

    #print(f'\033[1;33mANTES DO IF VARIAVEL RESP = {resp} O TIPE É {type(resp)}\033[m')
    if resp == 4:
        msg('Saindo do sistema até logo...', 1, 0, '_')
        return resp
    elif resp == 3:
        system('clear')
    elif resp == 2:
        cadastrar_dados()
        # pass
        # cadastrar uma nova pessoa e salvar em um arquivo
        # criar uma função para cadastrar
        # se o arquivo não existir criar uma arquivo
        # se o arquivo existir addicionar as novas informações no final do arquivo
        # msg('cadastrar uma nova pessoa e salvar em um arquivo')
        msg('', 0,1,'-')
        return resp
    elif resp == 1:
        mostrar_dados()
        # pass
        # mostrar o conteúdo de arquivo onde estão as pessoas cadastradas
        # criar uma função para mostrar 
        # msg('mostrar o conteúdo de arquivo onde estão as pessoas cadastradas')
        return resp
    else:
        print('Algo deu muito errado')
        return 666
    



# ======== PROGRAMA PRINCIPAL ==========
while True:
    msg('MENU PRINCIPAL', 1, 1, '=')
    opcoes() 
    msg('',1,0,'=')
    if escolha() == 4:
        break

