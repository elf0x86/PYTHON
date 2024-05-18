# todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
# usuário se ele quer ou não continuar a digitar valores.


soma = valor = maior = menor = media = tot_input = stop_condition = 0

while stop_condition != 999:
    valor = int(input("Digite um valor: "))
    soma += valor
    if stop_condition == 0:
        maior = valor
        menor = valor

    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor

    tot_input += 1
    stop_condition = int(input("[ 1 ]Continuar\n[ 999 ] Para sair."))

media = soma / tot_input
print(f'Total: {tot_input}')
print(f'Soma : {soma}')
print(f'Média: {media}')
print(f'Maior: {maior}, Menor: {menor}')

# Solução do video ------------------------------------------------------------------------------
resp = 'S'
soma = quant = media = maior = menor= 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
media = soma / quant
print(f'Você digitou {quant} numeros e a media foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
