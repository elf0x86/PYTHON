# Variaveis compostas  TUPLAS

lanche = 'Hamburguer'
lanche = 'Suco'
print(lanche)

print('=-=' * 30)

lancheira = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print(lancheira, type(lancheira))

print('=-=' * 30)

# Indexação
print(lancheira[1]) # Suco

print('=-=' * 30)

# Fatiamento
print(lancheira[-3])  # ultimo elemento
print(lancheira[1:3]) # de 1 até 3 não incluso
print(lancheira[2:])  # de 2 até o final
print(lancheira[:2])  # do inicio até elemento 2
print(lancheira[-2:]) # de -2 até o final -2 é Pizza  
print(lancheira[-3:]) # de -3 até o final -3 é Suco 

# Tuplas são imutaveis
# lancheira[0] = 'Refrigerange' # retorna erro TypeError: 'tuple' object does not support item assignment

print('=-=' * 30)

# Duas maneiras de fazer iteração de elementos de uma tupla
for LAN in lancheira:
    print(f'lanches da lancheira: {LAN}')

print('=-=' * 30)

# Esse metodo é usado quando prescisa mostrar os valores da tupla e a posição
for cont in range(0, len(lancheira)):
    print(f'Vou comer {cont}º --> {lancheira[cont]} ')

print('=-=' * 30)

# mostra os dados e a posição em variaveis diferentes
for pos, comida in enumerate(lancheira):
    print(f'Na posição {pos} temos {comida} para ingerir') 


print('=-=' * 30)
print(lancheira)
print(sorted(lancheira)) # sorted não muda a tupla em memoria. Ele transfora a tupla em uma lista temporaria
print(lancheira)
print('=-=' * 30)

a = (2, 5, 4, 2)
b = (5, 8, 1, 2)

print(f'tupla a: {a}')
print(f'tupla b: {b}')
c = a + b # concatena as tupla OBS: a ordem importa 

print(f'tupla c = a + b: {c}')
print(f'quantas vezes aparece o número 2 em c      --> {c.count(2)}')
print(f'qual é o index do numero 8 em c            --> {c.index(8)}')
print(f'apartir da posição 1 onde esta o proximo 2 --> {c.index(2, 1)}')


print('=-=' * 30)
# Tipos de dados diferentes na mesma tupla

pessoa = ('Gustavo', 38, 'M', 99.33, True)
print(f'pessoa: {pessoa}')
del(pessoa) # deleta da memoria serve para tuplas e outras variaveis
print(pessoa)
