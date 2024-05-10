# Ler o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa


cat_op = float(input("Comprimento cateto oposto: "))
cat_ad = float(input("Comprimento cateto adjacente: "))


hipo = (cat_op ** 2 + cat_ad ** 2) ** (1/2)

print(f"comprimento da hipotenusa é: {hipo:.2f}")
