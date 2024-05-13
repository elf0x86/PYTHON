import os

'''
# Conta de 0 a 9 (10 não é incluido) de 1 em 1
for x in range(0,10):
    print(f"Variavel de controle x: {x}. Ex: os.system('touch ARQUIVO_{x}.txt')")

# Conta de 0 a 9 (10 não é incluido) de 2 em 2
for x in range(0,10,2):
    print(f"Variavel de controle x: {x}. Ex: os.system('touch ARQUIVO_{x}.txt')")


# Conta de 10 a 0 de 1 em 1
for x in range(10, 0, -1):
    print(f"Variavel de controle x: {x}. Ex: os.system('touch ARQUIVO_{x}.txt')")
print('FIM')

# Conta de 10 a 0 de 1 em 2
for x in range(10, 0, -2):
    print(f"Variavel de controle x: {x}. Ex: os.system('touch ARQUIVO_{x}.txt')")
print('FIM')
'''
i = int(input('Início: '))
f = int(input('Fim   : '))
p = int(input('Passo : '))


escolha = int(input('Digite [ 1 ] para criar [ 0 ] para apagar ARQUIVO_X.txt: '))
for x in range(i,f+1,p):
    if escolha == 1:
        os.system(f'touch ARQUIVO_{x}.txt')
    elif escolha == 0:
        os.system(f'rm ARQUIVO_{x}.txt')
    else:
        print('Algo deu ERRADO!')
