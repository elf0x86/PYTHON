# Faça um programa que calcule a soma entre todos os números impares que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
todos = 0
for x in range(0, 500, 3): # multiplo de 3
    if x % 2 == 1:         # numeros  impares
        todos = todos + 1
        soma  = soma  + x

print(f'A soma de todos os {todos} valores solicitados é {soma}')

