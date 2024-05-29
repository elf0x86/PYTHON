# Crie um módulo chamado moeda.py que tenha as funções incorporadas...
# aumentar(), diminuir(), dobro() e metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções

import exe107_moeda

print('=' * 30)

p = float(input('Digite o preço R$: '))
print(f'A metade de {p} é {exe107_moeda.metade(p)}')
print(f'O dobro de  {p} é {exe107_moeda.dobro(p)}')
print(f'Aumentando 10%, temos {exe107_moeda.aumentar(p, 10)}')
print(f'Diminuidao 13%, temos {exe107_moeda.diminuir(p, 13)}')

print('=' * 30)
