# ler o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar 
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo


import datetime


ano_atual = int(datetime.date.today().year)

ano_nascimento = int(input("Ano de nascimento: "))
idade = ano_atual - ano_nascimento
print(f"Quem nasce em {ano_nascimento} tem {idade} anos em {ano_atual}")

if idade < 18:
    print(f'Ainda flatam {18 - idade} para o alistamento')
    print(f'Seu alistamento será em {(18 - idade) + ano_atual}')
elif idade == 18:
    print(f'Ano de alistamento militar')
elif idade > 18:
    print(f'Ja passou do ano de alistamento em {idade - 18} anos')
