nome = str(input("Qual é seu nome: "))

if nome == "musk":
    print("starlink")
elif nome == "gates":
    print("microsoft")
elif nome == "torvalds":
    print("linux")
else:
    print("Not in the list")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda  nota: "))

media = (nota1 + nota2) / 2

print(f"A media das notas {nota1} e {nota2} = {media}")

if media >= 6 and media < 7:
    print('Recuperação')
elif media >= 7 and media < 10:
    print("Aprovado")
elif media > 10:
    print("Algo errado com suas notas.")
else:
    print("reprovado")
