# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

times = ("Palmeiras", "Bahia","Flamengo","Botafogo","São Cruzeiro","Atlético","Bragantino",
         "Figueirence","Internacional","Fortaleza","Grêmio","Vasco","Criciúma","Juventude",
         "Barcelona","Corinthians","Fluminense","Vitória","Atlético","Cuiabá")

print('=' * 50)
print('Tabela do campeonato brasileiro')

print(f'{"Os 5 primeiros colocados são":=^50}')
for x in range(0, 5):
    print(f'{x}ª Colocado : {times[x]}')


print(f'{"Os 4 ultimos colocados são":=^50}')
for x in range(4, 0, -1):
    print(f'{(len(times) - x) + 1}ª Colocado : {times[-x]}')


#print(f'Os 5 primeiros colocados são: {times[0:5]}')
#print(f'Os 4 ultimos   colocados são: {times[-4:]}')
# retorna um erro e quebra o programa
# print(f'Posição da CHAPECOENSE {times.index("Chapecoence")}') 

print('=' * 50)
if 'Chapecoense' in times:
    print(f'Posição da CHAPECOENSE {times.index("Chapecoence")}') 
else:
    print(f'Chapeconese não esta na lista')

# Solução do video ------------------------------------------------------------
times = ("Palmeiras", "Bahia","Flamengo","Botafogo","São Cruzeiro","Atlético","Bragantino",
         "Figueirence","Internacional","Fortaleza","Grêmio","Vasco","Criciúma","Juventude",
         "Barcelona","Corinthians","Fluminense","Vitória","Atlético","Cuiabá")

print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Capecoense esta na {times.index("Chapecoense")+1} posição')


