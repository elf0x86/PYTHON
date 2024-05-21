# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta


expr = input('Digite a expressão: ')

if expr.count('(') == expr.count(')'):
    print('Sua expressão esta CERTA')
else:
    print('Sua expressão esta ERRADA')

