# Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Apple', 'Windows', 'Linux', 'Stallman', 'Guido')

print('=' * 40)
print(f'{"PALAVRA": <10} VOGAIS')
print('=' * 40)
for x in range(0, len(palavras)):
    print(f'{palavras[x]: <10} ', end='')
    for y in range(0, len(palavras[x])):
        if palavras[x][y].lower() in 'aeiouy':
            print(f'{palavras[x][y]} ', end='')
    print()
print('=' * 40)

# Solução do video ----------------------------------------------------------------------
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
