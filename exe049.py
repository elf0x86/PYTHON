# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher
# só que agora utilizando um laço for.

valor = int(input('Digite um número para ver sua tabuada: '))

for t in range(1, 11):
   # print(f'{valor} x {t:>2} = {valor*t}')
    print(f'{valor} x {t:>02} = {valor*t:>02}' if t < 10 else f'{valor} x {t} = {valor*t}')

