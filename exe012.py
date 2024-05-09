# ler o preço de um produto e mostre seu novo preço, com 5% de desconto.

pproduto = float(input("Preço do produto R$: "))

novo_pproduto = pproduto - (pproduto * 5 / 100)

print(f"O produto que custava R${pproduto}, na promoção com desconto de 5% vai custar R${novo_pproduto}")
