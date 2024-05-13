# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles : Dois lados iguais
# - Escaleno  : Todos os lados diferentes


seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo  segmento: ')) 
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima PODEM FORMAR um triângulo')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print('ISÓSCELES')
    elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')


