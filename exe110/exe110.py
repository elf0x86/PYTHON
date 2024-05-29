# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro
# a mais, informando se o valor retronado por elas vai ser ou não formatado pela função moeda()
# desenvolvida no desafio 108

import moeda

p = float(input('Digite o preço R$: '))
help(moeda.resumo)
moeda.resumo(p, 20, 10)
moeda.resumo(p, 20, 12)
