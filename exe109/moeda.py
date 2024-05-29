def aumentar(preco=0, taxa=0, formatacao=False):
    '''
    Aumento de um  valor monetario por uma taxa 
    :param preco:      recebe 0 como valor padrão
    :param taxa :      recebe 0 como valor padrão
    :param formatacao: recebe False como valor padrão
    :return:           res if not formatacao else moeda(res)
    '''

    res = preco + (preco * taxa / 100)
    if formatacao == True:
        return moeda(res)
    else:
        return res
#    return res if not formatacao else moeda(res)


def diminuir(preco=0, taxa=0, formatacao=False):
    '''
    Desconto de um  valor monetario por uma taxa 
    :param preco:      recebe 0 como valor padrão
    :param taxa :      recebe 0 como valor padrão
    :param formatacao: recebe False como valor padrão
    :return:           res if not formatacao else moeda(res)
    '''

    res = preco - (preco * taxa / 100)
    if formatacao == True:
        return moeda(res)
    else:
        return res
#    return res if not formatacao else moeda(res)


def dobro(preco=0, formatacao=False):
    '''
    Dobra um valor monetario pela metade
    :param preco:      recebe 0 como valor padrão
    :param formatacao: recebe False como valor padrão
    :return:           res if not formatacao else moeda(res)
    '''

    res = preco * 2
    if formatacao == True:
        return moeda(res)
    else:
        return res
#    return res if not formatacao else moeda(res)


def metade(preco=0, formatacao=False):
    '''
    Divide um valor monetario pela metade
    :param preco:      recebe 0 como valor padrão
    :param formatacao: recebe False como valor padrão
    :return:           res if not formatacao else moeda(res)
    '''

    res = preco / 2
    if formatacao == True:
        return moeda(res)
    else:
        return res
#    return res if not formatacao else moeda(res)


def moeda(preco, moeda='R$'):
    '''
    Formata a exibição de um valor monetario 
    :param preco: recebe um número inteiro ou float
    :param moeda: como a moeda vai ser exibida Ex: R$500,00
                  para R$ replace . to , as decimal separator
    :return: f'{moeda} {preco:.2f}'.replace('.', ',')
    '''


    return f'{moeda} {preco:.2f}'.replace('.', ',')
    # :8.2f -=-> 00000.00



