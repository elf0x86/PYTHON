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

