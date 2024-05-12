# Ler um númeor de 0 a 9999 e mostre na tela cada um dos dígitos separados.


numero = input("Informe um número: ")
print(f"Analisando o número: {numero}")
'''
Unidade= numero[0]
Dezena = numero[1]
Centena= numero[2]
Milhar = numero[3]
'''
nuero = int(numero)
Unidade= numero // 1 % 10 
Dezena = numero // 10 % 10
Centena= numero // 100 % 10
Milhar = numero // 1000 % 10

print(f"Unidade= {Unidade}")
print(f"Dezena = {Dezena}")
print(f"Centena= {Centena}")
print(f"Milhar = {Milhar}")
