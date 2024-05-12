# pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas


distancia = float(input('Qual é a distância da sua viagem? '))
preco     = 0

print(f'Você está prestes a começar uma viagem de {distancia:.2f}Km.')
print(f'O preço da sua passamge será de R$', end='')

if distancia <= 200:
    preco = distancia * 0.50
if distancia > 200:
    preco = distancia * 0.45  # desconto por andar mais Kilometros

print(preco)
