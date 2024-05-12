# ler um nome de uma pessoa e verificar se tem silva entre os nomes


nome = input("Nome completo: ").strip().lower()

print(f"Seu nome tem Silva? {'silva' in nome}")
