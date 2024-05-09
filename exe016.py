# leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: 6.127 --> 6
from math import trunc

number = float(input("Digite um número: "))
# parta_inteira = trunc(number)
# parta_inteira = int(number)
parta_inteira = number // 1

print(f"O número {number} tem a parte inteira {parta_inteira}")
