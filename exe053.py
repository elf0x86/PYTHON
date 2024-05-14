# Ler uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = input('Digite uma Frase: ').upper()
frase = ''.join(frase.split())
print(f'{frase} == {frase[-1::-1]}')

if frase == frase[-1::-1]:
    print('\033[1;32mTemos um palíndromo!')
else:
    print('\033[1;31mNão é um palíndromo.')

