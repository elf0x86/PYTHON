nome = str(input('Qual é sue nome? '))
if nome == 'Gustavo':
    print('youtuber do python')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular na lua de jupter')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Nome Feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')
