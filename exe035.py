import os
import time

print('-='*20)
print('Analisandor de Triângulos')
print('-='*20)


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo  segmento: '))
r3 = float(input('Terceiro segmento: '))

'''
os.system('sleep 0.5')
print('.', end='')
os.system('sleep 0.5')
print('.', end='')
os.system('sleep 0.5')
print('.', end='')
'''

time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
