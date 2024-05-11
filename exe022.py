# Leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome


nome = input("Ditgite seu nome completo: ")

print(f"Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)} letras e espaços")
total_de_letras = ''.join(nome.split())
print(f"Seu nome tem ao todo {len(total_de_letras)} letras")

nome = nome.split()

print(f"Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras")
