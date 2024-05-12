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

for x in range(0,8):
    cor += 1
    bac = 40
    for y in range(0,8):
        for z in range(0,4):
            print(sty[z], cor, bac)
            bac += 1
            if cor == 37:
                cor = 30
