n = 1
par = imp = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0: # vai funcionar somento se n for diferente de 0
        if n % 2 == 0: # analisa 0 como uma saída
            par = par + 1
        else:
            imp = imp + 1

print(f'Você digitou {par} numeros PARES e {imp} numeros IMPARES')
