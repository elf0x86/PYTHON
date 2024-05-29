def aumentar(valor=0, aumento=10):
    '''
    AUMENTA UM VALOR PASSADO EM 10% VEZES
    param: valor=10
    param: aumento=5
    return: valor + aumento
    '''
    porcentagem = (valor * aumento) / 100
    return valor + porcentagem 


def diminuir(valor=0, decremento=10):
    '''
    DIMIMUI UM VALOR PASSADO EM 10% VEZES
    param: valor=0
    param: decremento=100
    return: valor - aumento
    '''
    porcentagem = (valor * decremento) / 100
    return valor - porcentagem



def dobro(valor=10, dobro=2):
    '''
    DOBRA UM VALOR PASSADO EM 2 VEZES
    param: valor=10
    param: dobro=2
    return: valor * aumento
    '''
    return valor * dobro 


def metade(valor=10, metade=2):
    '''
    DIVIDE UM VALOR PASSADO EM 2 VEZES
    param: valor=12
    param: metade=2
    return: valor / aumento
    '''
    return valor / metade


