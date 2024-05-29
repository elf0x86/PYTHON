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


def resumo(preco=0, aumento=0, disconto=0):
    '''
    Faz um resumo e imprime uma mensagem formatada
    :param preco:    recebe um int ou float 
    :param aumento:  recebe um int ou float
    :param disconto: recebe um int ou float
    :return: 1
    '''

    msg = 'RESUMO DO VALOR'
    l_msg = len(msg) + 10
    print('-' * l_msg)
    print(f'{msg: ^{l_msg}}')
    print('-' * l_msg)

    print(f'{"Analisando preço": <{l_msg-7}}'      +  moeda(preco))
    print(f'{"Dobro do preço": <{l_msg-7}}'        +  dobro(preco, True))
    print(f'{"Metade do preço": <{l_msg-7}}'       +  metade(preco, True))
    print(f'{aumento}% {"de aumento": <{l_msg-11}}' +  aumentar(preco, aumento,  True))
    print(f'{disconto}% {"de redução": <{l_msg-11}}'+  diminuir(preco, disconto, True))

    return 1
