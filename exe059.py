# Ler dois valores e mostre um menu na tela
# [ 1 ] SOMAR
# [ 2 ] MULTIPLICAR
# [ 3 ] maior
# [ 4 ] Novos números
# [ 5 ] sair
# .: 
# Seu programa deverá realizar a operação solicitada em cada caso

msg = '=' * 40
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo  valor: '))
maior = v1
flag = 0

while flag != 5:
    flag = int(input('[ 1 ] SOMAR\n[ 2 ] MULTIPLICAR\n[ 3 ] maior\n[ 4 ] Novos números\n[ 5 ] sair\n.: '))
    if flag == 1:
        print(msg)
        print(f'A SOMA entre {v1} + {v2} = {v1 + v2}')
        print(msg)
    if flag == 2:
        print(msg)
        print(f'A MULTIPLICAÇÃO entre {v1} x {v2} = {v1 * v2}')
        print(msg)
    if flag == 3:
        if v2 > maior:
            maior = v2
        else:
            maior = v1
        print(msg)
        print(f'O maior valor é {maior}')
        print(msg)
    if flag == 4:
        print(msg)
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo  valor: '))


