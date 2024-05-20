# Desenvolva um programa que leia quatro valores teclado e gurade-os em uma
# TUPLA. No final mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os núemros pares

valores = (input('Valor: '), input('Valor: '), input('Valor: '), input('Valor: '))    

print(valores)
print('-' * 40)
print(f'Quantas vezes aparece o 9? {valores.count("9")}')
if "3" in valores:
    print(f'Em que posição foi digitado o primeiro valor 3? {valores.index("3")}')
else:
    print('\033[1;33O valor 3 não foi inserido!\033[m')
print('Os valores pares digitados foram ', end='')

for p in valores:
    if p.isdigit():
        if int(p) % 2 == 0:
            print(f'{p} ', end='')
print()
print('-' * 40)


# Solução do video ------------------------------------------------------------------

num = (int(input('Digite um número: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
