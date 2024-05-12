# ler o nome de uma cidade e diga se ela começa ou não com o nome 'santo'

cidade = input("Em que cidade você nasceu? ").lower()

#print(cidade.find('santo'))
#print('santo' in cidade)
cidade = cidade.strip()
print(cidade[:5] == 'santo')
