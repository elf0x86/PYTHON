# Mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:
        print(f'{n}', end=' ')
print('acabou')

for n in range(2, 51, 2):
    print('.', end='')
    print(f'{n}', end=' ') # usa a metado do tempo para executar 
print('acabou')
