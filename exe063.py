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


