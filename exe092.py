# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionario se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
# vai se aposentar.
import datetime

ano_atual = datetime.datetime.today().year
pessoa = dict()
pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de Nascimanto: '))
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario R$: '))

print('-=' * 40)
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')

