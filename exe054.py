# Ler o ano de nascimento de sete pessoas. No final mostrar quantas pessoas ainda não atingiram a
# maior idade e quantas já são maiores.
from datetime import date


maior = 0
menor = 0
idade = 0
ano   = 0

for x in range(0, 7):
    ano   = int(input(f'Em que ano a {x}º pessoa nasceu? '))
    idade = date.today().year - ano
    if idade >= 18:
        maior += 1
    elif idade < 18:
        menor += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'Ao todo tivemos {menor} pessoas monores de idade')


