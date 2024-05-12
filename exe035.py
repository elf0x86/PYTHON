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


time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.', end='')
'''

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):


    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()


# A List of Items
items = list(range(0, 57))

# A Nicer, Single-Call Usage
for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
    # Do stuff...
    time.sleep(0.1)




if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
