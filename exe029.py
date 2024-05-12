# Ler a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa var custar R$7.00 por cada Km acima do limite


velocidade = float(input("Qual é a velocidade atual do carro? "))
multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Multado! Você exedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${multa}')
print(f'Tenha um bom dia! Dirija com segurança!')
