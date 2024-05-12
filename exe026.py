# ler uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'A'.
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.


frase = input("Digite uma frase: ").strip().lower()

print(f"letra 'A' aparece {frase.count('a')} vezes na frase")
print(f"primeira letra 'A' apareceu na posição {frase.find('a')}")
print(f"a ultima letra 'A' apareceu na posição {frase.rfind('a')}")
