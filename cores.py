cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'preto_branco': '\033[7:30m'
         }

print(f'{cores["azul"]}Testando cores{cores["limpa"]}')


# 256 different possibilities


cor = 29
bac = 40
sty = [0,1,4,7]

for a in range(0,8):
    cor += 1
    bac = 40
    for b in range(0,8):
        for x in range(0,4):
            print(sty[x], cor, bac, f'\033[{sty[x]};{cor};{bac}mTESTANDO CORES\033[m')

        bac += 1
#    print('-'*30)

