test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test) # Faz um LINK da lista test para dentro da lista galera 
print(galera)
test[0] = 'Maria'    
test[1] = 22
galera.append(test) 
print(galera)

print('=' * 40)

test = list()
test.append('Gustavo')
test.append(40)
galera = list()
galera.append(test[:])  # Faz uma COPIA de todos os dados para dentro de galera
print(galera)
test[0] = 'Maria'
test[1] = 22
galera.append(test)
print(galera)


print('=' * 40)
pessoal = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoal)
print(pessoal[0])
print(pessoal[0][0])
print(pessoal[2][1])

print('-' * 40)
for p in pessoal:
    print(p)

print('-' * 40)
for n in pessoal:
    print(n[0])

print('-' * 40)
for i in pessoal:
    print(i[1])

print('-' * 40)
for fulano in pessoal:

    print(f'{fulano} --> {fulano[0]: >10} tem {fulano[1]: >10} anos de idade')

print('=' * 40)
galera = list()
dado = list()

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)
    galera.append(dado[:])
    dado.clear()
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)

print('=' * 40)
galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)
    galera.append(dado) # OBSERVE
    dado.clear() # Quando dou clear no dado() tamber dou clear() na galera
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)

print('=' * 40)
galera = list()
dado = list()
tot_maior = tot_menor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)
    galera.append(dado[:])
    dado.clear()
    print(f'dado: {dado}')
    print(f'galera: {galera}')
    print('_' * 40)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        tot_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        tot_menor += 1
print(f'Temos {tot_maior} maior(es) e {tot_menor} menor(es) de idade')

