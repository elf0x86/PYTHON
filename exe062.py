# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerra quando ele disser que quer mostror 0 termos

count = 1
termo_inicio = int(input('Termo da PA: '))
razao_passo  = int(input('Razão: '))
ultimo_termo = 0
continuar    = 1
msg = ''

while continuar != 0:
    while count != 10:
        # print(f'{termo_inicio} ', end='') 
        msg += f'{termo_inicio} '
        termo_inicio += razao_passo
        ultimo_termo = termo_inicio

        count += 1

    print(msg)
    continuar = int(input(f'[ 1 ] Para mostrar mais 10 Termos\n[ 0 ] Para sair\n.:'))
    count = 1


