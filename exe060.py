# Faça um programa que leia um número qualquer e mostre o seu fatorial
# 5! 5x4x3x2x1

num = int(input("Ver fatorial de: "))
tot = 1

print(f'{num}! = ', end='')
for x in range(num, 0, -1):
    if x == num:
        tot = x
        print(f'{x}x',end='')
    elif x > 1:
        tot = tot * x
        print(f'{x}x',end='')
    else:
        print('1', end='')

print(f' = {tot}')
