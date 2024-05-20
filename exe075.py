# Desenvolva um programa que leia quatro valores teclado e gurade-os em uma
# TUPLA. No final mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3


valores = (input('Valor: '), input('Valor: '), input('Valor: '), input('Valor: '))    

print(valores)
print('-' * 40)
print(f'Quantas vezes aparece o 9? {valores.count("9")}')
print(f'Em que posição foi digitado o primeiro valor 3? {valores.index("3")}')
print('-' * 40)
