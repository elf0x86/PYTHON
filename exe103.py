# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# O nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente

def ficha(nome='<desconhecido>', gols=0):
    '''
    FICHA DE UM JOGADOR
    param nome: recebe uma string 
    param gols: recebe um  inteiro
    Ex:
    ficha('Ronaldo', 3) -> O jogador Ronaldo fez 3 gol(s) no campeonato
    ficha('Kaka')       -> O jogador Kaka fez 0 gol(s) no campeonato
    ficha(3)            -> O jogador <desconhecido> fez 3 gol(s) no campeonato
    '''

    if type(nome) == int:
        gols = nome
        msg  = f'O jogador <desconecido> fez {gols} gol(s) no campeonato'
    elif nome == '' and gols != '':
        msg = f'O jogador <desconecido> fez {gols} gol(s) no campeonato'
    elif gols == '':
        msg = f'O jogador <desconecido> fez 0 gol(s) no campeonato'
    else:
        msg = f'O jogador {nome} fez {gols} gol(s) no campeonato'
    print('-' * len(msg))
    print(msg)

nome = input('Nome do jogador: ')
gols = input('Número de GOLS: ')
ficha(nome, gols)
help(ficha)
'''
ficha()
ficha('Ronaldo', 3)
ficha(nome)
ficha(gols)

jogador_1 = ficha()
jogador_2 = ficha('Ronaldo', 3)
jogador_3 = ficha('Kaka')
jogador_4 = ficha(3)

print(jogador_1)
print(jogador_2)
print(jogador_3)
print(jogador_4)
'''
# ================= SEGUNDA TENTATIVA IDEIA ================= 
def ficha(nome='<desconhecido>', gols='0'):
    '''
    FICHA DE UM JOGADOR
    param nome: recebe uma string 
    param gols: recebe um  inteiro
    Ex:
    ficha('Ronaldo', 3) -> O jogador Ronaldo fez 3 gol(s) no campeonato
    ficha('Kaka')       -> O jogador Kaka fez 0 gol(s) no campeonato
    ficha(3)            -> O jogador <desconhecido> fez 3 gol(s) no campeonato
    '''

    if nome == '<desconhecido>' or nome == '' and gols == '0' or gols == '':
        return f'O jogador {nome} fez {gols} gol(s) no campeonato'
    elif nome != '' and gols == '0': 
        return f'O jogador {nome} fez 0 gol(s) no campeonato'

    if nome.isdigit():
        tmp = nome
        gols = tmp
        nome = '<desconhecido>'
        return f'O jogador {nome} fez {gols} gol(s) no campeonato'



# Versão que imprime os valores passando os argumentos literalmente HARDCODED
'''
ficha()
ficha(3)
ficha('Ronaldo')
ficha('Ronaldo', 3)
ficha(gols=3, nome='Juca')

'''
NOME = input('Nome do jogador: ')
GOLS = input('Número de GOLS: ')
print(f'NOME =========================> ', NOME)
print(f'GOLS =========================> ', GOLS)
print('ficha() ----------------------> ', ficha())
print('ficha(GOLS) ------------------> ', ficha(GOLS))
print('ficha(NOME) ------------------> ', ficha(NOME))
print('ficha(NOME, GOLS) ------------> ', ficha(NOME, GOLS))
print('ficha(GOLS, NOME) ------------> ', ficha(GOLS, NOME))
print('ficha(gols=GOLS, nome=NOME) --> ', ficha(gols=GOLS, nome=NOME))
print('ficha(nome=NOME, gols=GOLS) --> ', ficha(nome=NOME, gols=GOLS))
# help(ficha)

# ================= TERCEIRA TENTATIVA IDEIA ================= 
def ficha(nome='<desconhecido>', gols=0):
    '''
    FICHA DE UM JOGADOR
    param nome: recebe uma string 
    param gols: recebe um  inteiro
    Ex:
    ficha('Ronaldo', 3) -> O jogador Ronaldo fez 3 gol(s) no campeonato
    ficha('Kaka')       -> O jogador Kaka fez 0 gol(s) no campeonato
    ficha(3)            -> O jogador <desconhecido> fez 3 gol(s) no campeonato
    '''

    if nome == '<desconhecido>' and gols == '' or gols == 0:
        msg = f'O jogador <desconecido> fez 0 gol(s) no campeonato'
        return 0
    if str(nome).isnumeric(): 
        msg = f'O nome tem que ser um NOME e não numeros'
        return 0

    if nome != '' and gols == 0:
        msg = f'O jogador {nome} fez 0 gol(s) no campeonato'
        return 0 
    if nome != '' and int(gols) >= 0:
        msg = f'O jogador {nome} fez {gols} gol(s) no campeonato'
        return 0
    '''
    if type(gols) == int:
        gols = str(gols)
    
    else:
        if nome == '' and gols == '':
            msg = f'O jogador <desconecido> fez 0 gol(s) no campeonato'

        if nome == '' and gols.isdigit():
            msg = f'O jogador <desconecido> fez {gols} gol(s) no campeonato'

        if (type(nome) == str and nome != '') and gols.isdigit():
            msg = f'O jogador {nome} fez {gols} gol(s) no campeonato'

        if (type(nome) == str and nome != '') and gols == '':
            msg = f'O jogador {nome} fez 0 gol(s) no campeonato'
    '''
    print(msg)

# Versão que imprime os valores
print('ficha() -->', end=' ')
ficha()

print('ficha(3) -->', end=' ')
ficha(3)

print('ficha("Ronaldo") -->', end=' ')
ficha('Ronaldo')

print('ficha("Ronaldo", 3) -->', end=' ')
ficha('Ronaldo', 3)




'''
nome = input('Nome do jogador: ')
gols = input('Número de GOLS: ')


ficha()
ficha(gols)
ficha(nome)
ficha(nome, gols)


# Versão retorna os valores
jogador_1 = ficha()
jogador_2 = ficha(3)
jogador_3 = ficha('Ronaldo')
jogador_4 = ficha('Ronaldo', 3)

jogador_5 = ficha()
jogador_6 = ficha(gols)
jogador_7 = ficha(nome)
jogador_8 = ficha(nome, gols)
'''


# SOLUÇÃO DO VIDEO ------------------------------------------------------------------------
def ficha_v1(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')
# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols : '))
if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.stri() == '':
    ficha(gol=g)
else:
    ficha(n, g)

