print('DECLARAR UMA LISTA')
num = [2, 5, 9, 1]
tmp = list()
print(num)

print('SUBSTITUIR UM VALOR DE UM INDICE ESPECIFICO')
num[2] = 3
print(num)

print('ADDICIONAR UM VALOR NO FINAL DA LISTA')
# num[4] = 6 # lista out of index
num.append(6)
print(num)

print('ADDICIONAR UM VALOR EM UM INDICE ESPECIFICO')
num.insert(2, 7)
print(num)

print('COLOCAR A LISTA DE NUMEROS EM ORDEM CRESCENTE')
num.sort()
print(num)

print('COLOCAR A LISTA DE NUMEROS EM ORDEM DECRESCENTE')
num.sort(reverse=True)
print(num)

print('OBTER QUANTOS ELEMENTOS TEM EM UMA LISTA')
tamanho = len(num)
print(f'Essa lista tem {tamanho} elementos')

print('ELIMINAR O ULTIMO ELEMENTO')
removed = num.pop() # .pop() remove o ultimo elemento por padrão e retorna o valor
print(num, removed)

print('ELIMINAR UM ELEMENTO INDICADO POR UM INDICE')
removed = num.pop(2) # .pop() remove o ultimo elemento por padrão e retorna o valor
print(num, removed)

print('ELIMINAR A PRIMEIRA OCORRENCIA DE UM ELEMENTO APARTIR DO INICIO DA LISTA')
num = [1, 3, 4, 3, 8]
print(num, 'eleiminar o número 3')
num.remove(3)
print(num)


print('REMOVENTO TODOS OS ELEMENTOS REPETIDOS DE UMA LISTA')
num = [1, 3, 4, 3, 8, 3]
print(num)
for i in range(0, len(num)):
    if 3 in num:
        num.remove(3)
    print(num)



print('=' * 40)
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...')

for cont in range(0, 5):
    valores.append(int(input('Valor: ')))


for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print(valores)
print('Cheguei ao final da lista')


print('=' * 40)
print('LIGAçÃO DE LISTA list_a = list_b CRIA UMA LIGAÇÃO ENTRE ELAS')
print('=' * 40)
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}') 
print(f'Lista B: {b}') # a saída é a mesma de A


print('=' * 40)
print('COPIA DE DADOS DE UMA LISTA list_a = list_b[:] copia todos elementos de list_b para list_a')
print('=' * 40)
list_a = [1,2,3,4]
list_b = list_a[:]
list_b[2] = 77
print(f'Lista A: {list_a}')
print(f'Lista B: {list_b}')


