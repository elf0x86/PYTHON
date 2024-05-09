# Ler um valor em metros e o exiba convertido em centímetros e milímetros

metros = int(input("Qual é o valor em metros: "))

metros_para_centimetros = metros * 100
metros_para_milimetros  = metros * 1000

print(f"{metros}M = {metros_para_centimetros:.0f}cm")
print(f"{metros}M = {metros_para_milimetros:.0f}mm")

medida = float(input("Digite um valor: "))

dm  = medida * 10
cm  = medida * 100
mm  = medida * 1000
dam = medida / 10
hm  = medida / 100
km  = medida / 1000
