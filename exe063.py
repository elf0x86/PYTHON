# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
# primeiros elementos de uma Sequência de Fibonacci.
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8


n = int(input('Mostrar N fibonacci Numbers: '))
t1 = 0
t2 = 1
t3 = 0

while n != 0:
   t3 = t1 + t2
   if n > 1:
       print(f'{t3} -> ', end='')
   if n == 1:
       print(f'{t3}')
   t2 = t1
   t1 = t3

   n -= 1

# Solução do video -----------------------------------------------------------------------
print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} -> {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')

# 0 - 1 - 1
# t1 t2  t3

# 0 - 1 - 1 - 2
#    t1  t2  t3

# 0 - 1 - 1 - 2 - 3
#        t1  t2  t3

# 0 - 1 - 1 - 2 - 3 - 5
#            t1  t2  t3

# 0 - 1 - 1 - 2 - 3 - 5 - 8
#                t1  t2  t3



