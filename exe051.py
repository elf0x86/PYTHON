# Ler o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão

menu='='*30
msg='10 TERMOS DE UMA PA'
print(menu)
print(f'{msg:-^30}')
print(menu)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for x in range(termo, 20, razao):
    print(f'{x} -> ', end='')
print('ACABOU')



# Forma para saber o enésimo termo de uma PA
decimo = termo + (10 - 1) * razao

for x in range(termo, decimo + razao, razao):
    print(f'{x} -> ', end='')
print('ACABOU')


