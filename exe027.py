# ler o nome completo de uma pessoa mostrando em seguda o primeiro e o último
# nome separadamente


nome_completo = input("Digite seu nome completo: ")
print(f"Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome_completo.split()[0]}")
print(f"Seu último   nome é {nome_completo.split()[-1]}")
