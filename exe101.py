# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(ano_nascimento=0):
    '''
    :param ano_nascimento: Recebe um número inteiro do ano de nascimento
                            Se o parametro não receber um valor na chamada da função
                            ele recebe o valor padrão 0
    '''
    # ESCOPO DE IMPORTAÇÃO DENTRO DE UMA FUNÇÃO
    import datetime

    if ano_nascimento == 0:
        print(f'\033[1;34mO ano de nascimento não foi informado\033[m')
        return 0
    else:
        print('-' * 30)
        ano_atual = datetime.datetime.today().year
        idade     = ano_atual - ano_nascimento

        if idade >= 18 and idade < 60:
            return f'com {idade} anos: VOTO OBRIGATORIO'
        elif idade >= 60:
            if idade > 110:
                return f'Você é uma anciao das antigas! VOTO OPCIONAL meu SENHOR.'
            else:
                return f'com {idade} anos: VOTO OPCIONAL'
        elif idade < 18 and idade > 0:
            return f'com {idade} anos: NÃO VOTA'
        else:
            return f'\033[1;33mIdade de << {idade} >> Você vem do FUTURO?\033[m'

# Programa principal
help(voto)
print(voto())
print(voto(1993))
print(voto(2015))

# SOLUÇÃO DO VIDEO -------------------------------------------------------------------------------
# from datetime import date  # É IMPORTADA PARA O PROGRAMA INTEIRO

def voto(ano):
    # ESCOPO DE IMPORTAÇÃO
    from datetime import date # a classe date só vai ficar na memória durante a execução Economizando memória :)

    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos NÃO VOTA'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos VOTO OPCIONAL'
    else:
        return f'Com {idade} anos VOTO OBRIGATÓRIO'


print(voto(2000))
print(voto(2010))
print(voto(1990))
# mes = date.today.month # Já não funciona mais prq o import global foi comentado
