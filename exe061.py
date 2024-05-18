# Refaça o DESAFIO 051 lendo o primeiro termo e a razão de uma PA,
# mostrando so 10 primeiros termos da progressão usando etrutura while


count = 1
termo_inicio = int(input('Termo da PA: '))
razao_passo  = int(input('Razão: '))


while count != 11:
    print(f'{termo_inicio} ', end='') 
    termo_inicio += razao_passo
    count += 1
print('--- FIM')
