# Sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada

import random

alunos = input("Digite quatro nomes separados por Espaços: ")
alunos = alunos.split()

random.shuffle(alunos)
print(alunos)
random.shuffle(alunos)
print(alunos)
random.shuffle(alunos)
print(alunos)
random.shuffle(alunos)

print('-'*80)
print('FINAL RESULT:---> ', alunos)
print('-'*80)
