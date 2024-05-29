# Adapte o código do desafio 107, criando uma funçõa adicional
# chamada moeda() que consiga mostrar os valores como um valor
# monetário formatado.

# from exe108 import moeda # erreo de (most likely due to a circular import)
import moeda

p = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(p)} é\t{moeda.moeda(moeda.metade(p))}')
print(f'O dobro  de {moeda.moeda(p, "R¥")} é\t{moeda.moeda(moeda.dobro(p), "R¥")}')
print('-' * 40)
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuidao 13%, temos {moeda.moeda(moeda.diminuir(p, 13), "R¥")}')

