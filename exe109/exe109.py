# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
# a mais, informando se o valor retronado por elas vai ser ou não formatado pela função moeda()
# desenvolvida no desafio 108

import moeda

p = float(input('Digite o preço R$: '))

metade   = moeda.metade(p, True)
dobro    = moeda.dobro(p, True)
aumento  = moeda.aumentar(p, 10, True)
desconto = moeda.diminuir(p, 20, True)

print('=' * 40)
print(f'A metade de {moeda.moeda(p, "R$")} é\t{metade}')
print(f'O dobro  de {moeda.moeda(p, "R$")} é\t{dobro}')
print('-' * 40)
print(f'Aumentando 10%, temos {aumento}')
print(f'Diminuidao 13%, temos {desconto}')
print('=' * 40)

help(moeda.metade)
help(moeda.dobro)
help(moeda.aumentar)
help(moeda.diminuir)
help(moeda.moeda)
