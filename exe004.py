# leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

dado = input("Digite algo: ")

print(f"é alphanumerico : {dado.isalpha()}")
print(f"é decimal       : {dado.isdecimal()}")
print(f"é digito        : {dado.isdigit()}")
print(f"é indentificador: {dado.isidentifier()}")
print(f"é lowrcase      : {dado.islower()}")
print(f"é numerico      : {dado.isnumeric()}")
print(f"é imprimivel    : {dado.isprintable()}")
print(f"é espaço        : {dado.isspace()}")
print(f"é maiuscolo     : {dado.isupper()}")
print(f"inicial em maiusculo: {dado.istitle()}")
