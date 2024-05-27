# Faça um programa que tenha um função chamada área() que receba as dimensões
# de um terreno retangular (largura, comprimento) e mostre a area do terreno


def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m².')

area(float(input(f'LARGUR (m): ')), float(input(f'COMPRIMENTO (m): ')))



# SOLUÇÃO DO VIDEO ----------------------------------------------------
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area:.1f}m².')

# Programa principal
print(' Controle de Terrenos')
print('-' * 20)


l = float(input(f'LARGUR (m): '))
c = float(input(f'COMPRIMENTO (m): '))
area(l, c)
