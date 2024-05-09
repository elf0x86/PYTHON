# ler o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Qual é seu salario: "))
novo_salario = salario + (salario * 15 / 100)

print(f"Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${novo_salario}")
