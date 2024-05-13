import os


'''
for x in range(0,10):
    print(f"Variavel de controle x: {x}. Ex: os.system('touch ARQUIVO_{x}.txt')")
print('FIM')
'''

escolha = int(input('Digite [ 1 ] para criar [ 0 ] para apagar ARQUIVO_X.txt: '))
for x in range(0,10):
    if escolha == 1:
        os.system(f'touch ARQUIVO_{x}.txt')
    elif escolha == 0:
        os.system(f'rm ARQUIVO_{x}.txt')
    else:
        print('Algo deu ERRADO!')


