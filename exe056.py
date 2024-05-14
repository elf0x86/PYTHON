# Ler o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homen mais velho
# - Quantas mulhers tem menos de 20 anos

media              = 0
mais_velho_M_idade = 0
mais_velho_M_nome  = '' 
total_F_menores    = 0

for x in range(1, 5):
    print(f'----- {x}º PESOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    media += idade
    sexo = input('Sexo [M/F]: ').upper()

    if idade < 20 and sexo == 'F':
        total_F_menores += 1

    if x == 1:
        #print(f'Valor de x {x}, idade = {mais_velho_M_idade}, nome = {mais_velho_M_nome}')
        mais_velho_M_idade = idade
        mais_velho_M_nome  = nome


    if idade > mais_velho_M_idade and sexo == 'M':
            mais_velho_M_idade = idade
            mais_velho_M_nome  = nome 
            #print(f'Valor de x {x}, idade = {mais_velho_M_idade}, nome = {mais_velho_M_nome}')

print(f'A média de idade do grupo é de {media / 4} anos')
print(f'O homen mais velho tem {mais_velho_M_idade} anos e se chama {mais_velho_M_nome}')
print(f'Ao todo são {total_F_menores} mulheres com menos de 20 anos')
