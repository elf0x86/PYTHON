nome = input("Qual seu nome: ")
print(f"Ola {nome:<20}, seja bem vindo")  # Ola Guanabara           , seja bem vindo
print(f"Ola {nome:>20}, seja bem vindo")  # Ola            Guanabara, seja bem vindo
print(f"Ola {nome:^20}, seja bem vindo")  # Ola      Guanabara      , seja bem vindo
print(f"Ola {nome:=^20}, seja bem vindo") # Ola =====Guanabara======, seja bem vindo
print(f"Ola {nome:=<20}, seja bem vindo") # Ola Guanabara===========, seja bem vindo
print(f"Ola {nome:=>20}, seja bem vindo") # Ola ===========Guanabara, seja bem vindo


print(f"Ola {nome.upper():=^20}, seja bem vindo")     # Ola =====GUANABARA======, seja bem vindo
print(f"Ola {nome[4:].upper():=^20}, seja bem vindo") # Ola =======ABARA========, seja bem vindo

numero = 1.333333
print(f"Original {numero}, Modificado {numero:.2f}") # Original 1.333333, Modificado 1.33



