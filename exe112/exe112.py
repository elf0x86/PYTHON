from utilidadescev import moeda, dado


# p = float(input('Digite o preço R$: '))
p = dado.leiaDinheiro('Digite o preço: ')
# help(moeda.resumo)
moeda.resumo(p, 20, 10)
moeda.resumo(p, 20, 12)
