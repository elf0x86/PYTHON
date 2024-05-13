# Faça um programa que mostre na tela uma contagem regresiva para o lançamento do starlink.
# Indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time


frutas=['jaca', 'apple', 'orange', 'banana', 'morango', 'uva', 'tomate', 'melancia', 'nona', 'tangerina', 'abacaxi']

for x in range(10, -1, -1):
    print(x, frutas[x])
    time.sleep(0.8)
print('BOOM BOOM POOW')

for x in range(0, 11):
    print(x, frutas[x])
    time.sleep(0.8)
print('BOOM BOOM POOW')
