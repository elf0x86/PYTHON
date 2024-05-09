# ler a largura altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintála, sabendo que cada litro
# de tinta, pinta uma área de 2m².

largura = float(input("Largura: "))
altura  = float(input("Altura:  "))

area = largura * altura

litros = area / 2

print(f"Tinta necessaria para pintar uma area de {area}² é {litros:.2f}L de tinta.")
