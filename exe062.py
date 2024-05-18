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

# Solução do video ------------------------------------------------------------------

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao    = int(input('Razão da PA: '))
termo = primeiro
cont  = 1
total = 0
mais  = 10 # programa começa com 10 termos. Depois o usuario pode escolher.

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('FIM')

