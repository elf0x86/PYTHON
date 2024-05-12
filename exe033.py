# Ler três números e mostre qual é o maior e qual é o menor

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor : '))
c = int(input('Terceiro valor: '))

'''
if a < b and a < c:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
'''

menor = a  # assumir que é o menor 
nome_input = 'a'
if b < a and b < c:
    menor = b
    nome_input = 'b'
if c < a and c < b:
    menor = c
    nome_input = 'c'

print(f'O menor valor é {menor} e o nome da variavel é: {nome_input}')

maior = a  # assumir que é o menor 
nome_input2 = 'a'
if b > a and b < c:
    maior = b
    nome_input = 'b'
if c > a and c < b:
    maior = c
    nome_input = 'c'

print(f'O maior valor é {maior} e o nome da variavel é: {nome_input2}')
