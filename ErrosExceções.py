'''
while True:

    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
        print(f'O resultado é {r}')
        break
    except:
        print(f'\033[1;31mInfelizmente tivemos um problema :(\033[m')
        continue


while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
        print(f'O resultado é {r:.2f}')
        break
    except:
        print(f'\033[1;31mInfelizmente tivemos um problema :(\033[m')
        print(f'E qual foi o erro?')
        continue
    # clausolas opcionais
    else:
        print(f'\033[1;32mPassando para avisar que o programa funcionou! :)\033[m')
    finally:
        print(f'\033[1;36;48mCerto ou Errado o negocio é tentar\033[m')

while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
        print(f'O resultado é {r}')
        break
    except Exception as eRRo:
        print(f'\033[1;31mInfelizmente tivemos um problema :(\033[m')
        print(f'E qual foi o erro? --> {eRRo.__class__}')
        continue
    # clausolas opcionais
    else:
        print(f'\033[1;32mPassando para avisar que o programa funcionou! :)\033[m')
    finally:
        print(f'\033[1;36;48mCerto ou Errado o negocio é tentar\033[m')

'''


while True:
    try:
        print('\033[4;33;44mSó aceitamos valores inteiros\033[m')
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
        print(f'O resultado é {r}')
        break
    except ValueError:
        print('\033[1;37;42mVOCÊ ENTROU COM UM VALOR MUITO ERRADO BABY!\033[m')
    except Exception as eRRo:
        print(f'\033[1;31mInfelizmente tivemos um problema :(\033[m')
        print(f'E qual foi o erro? --> {eRRo.__class__}')
        continue
   # clausolas opcionais
    else:
        print(f'\033[1;32mPassando para avisar que o programa funcionou! :)\033[m')
    finally:
        print(f'\033[1;36;48mCerto ou Errado o negocio é tentar\033[m \033[1;31m<3\033[m')

