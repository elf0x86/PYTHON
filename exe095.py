# Aprimore o DESAFIO 093 para que ele foncione com vários jogadores, incluindo um sistema de visualização
# de datalhes do aproveitamento de cada jogador.

jogador   = dict()
jogadores = list()
partidas  = []
gols      = 0

while True:
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for x in range(0, jogador['partidas']):
        partidas.append(int(input(f'Total de gols na partida {x}: ')))
        gols += partidas[x]

    jogador['tot_gols_por_partida'] = partidas[:]
    jogador['total'] = gols


    jogadores.append(jogador.copy())

    partidas.clear()
    jogador.clear()
    gols = 0

    resp = input('\033[1;32mQuer continuar [S/N]: \033[m').strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 40)

print(f'COD\tNOME\t\tGOLS\t\tTOTAL')
print('--' * 40)
for j in range(0, len(jogadores)):
    print(f'{j}\t{jogadores[j]["nome"]}\t\t{jogadores[j]["tot_gols_por_partida"]}\t\t{jogadores[j]["total"]}')

print('--' * 40)
while True:
    resp = int(input('\033[1;32mMostrar dados de qual jogador: \033[m'))
    if resp == 999:
        break

    if resp > len(jogadores[resp]['tot_gols_por_partida']): # RETORNA UM ERRO DE LIST OUT OF RANGE <<< RESOLVER COM TRATAMENTO DE ERRO >>>
        print('\033[1;33mNUMERO DO JOGADOR INVALIDO\033[m')
    else:
        print(f'-- Levantamento do jogador {jogadores[resp]["nome"]}')
        for j in range(0, len(jogadores[resp]['tot_gols_por_partida'])): 
            print(f'No jogo {j} fez {jogadores[resp]["tot_gols_por_partida"][j]} gols.')
    print('--' * 40)

print('<<< VOLTE SEMPRE >>>')

# SOLUÇÃO DO VIDEO ------------------------------------------------------------------------------------
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:] 
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
   
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print (f'{k:<3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
