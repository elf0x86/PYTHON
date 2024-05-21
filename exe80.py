# Crie um programa onde o usuário possa digitar cinco valores numericos e cadastre-os em uma lista
# já na posição correta de inserção (sem usar o sort()). No final mostre a lista ordenada na tela

# Solução do video -------------------------------------------------------------------------------
lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    '''
    # 3 possibilidades [ou ele é o primeiro, ou o ultimo, ou vai estar no meio]
    if c == 0:
        lista.append(n)
    elif n > lista[len(lista)-1]: # n é maior que o número do ultima posição da lista --> lista[-1]
        lista.append(n)
    '''
    if c == 0 or n > lista[-1]: # verifica se n vai entrar na posição 0 ou na ultima posição da lista
        lista.append(n)
        print(f'Adicionado no final da lista...{lista}')
    else: # verifica se vai entrar no meio da lista
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...{lista}')
                break
            pos += 1


print('-' * 30)
print(f'Os valores digitados em eordem foram {lista}')

