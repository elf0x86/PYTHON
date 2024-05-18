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

# Solução do video --------------------------------------------------------
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo  valor: '))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] soma
    [ 2 ] multiplicar
    [ 3 ] maior 
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual sua opcão? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A sooma entre {n1} + {n2} = {soma}')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} = {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo  valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')

