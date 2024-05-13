# ler duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida
# -Média abaixo de 5.0   : REPROVADO
# -Média entre  5.0 e 6.9: RECUPERAÇÃO
# -Média entre  7.0 ou superior: APROVADO


nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda  nota: "))

media = (nota1+nota2) / 2

print(f'Nota {nota1} e {nota2}, a média do aluno é {media}')

if media >= 7 and media <= 10:
    print(f'O aluno esta APROVADO')
elif media >= 5 and media <= 6.9:
    print(f'O aluno esta de RECUPERAÇÃO')
elif media < 5 and media >= 0:
    print(f'O aluno esta REPROVADO')
else:
    print('Algo deu ERRADO.')

