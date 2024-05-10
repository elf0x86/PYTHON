# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import randint

aluno = input("Primeiro nome de quatro alunos: ")
aluno = aluno.split()
print(f"O aluno sorteado para apagar o quadro é: {aluno[randint(0,3)]}")
