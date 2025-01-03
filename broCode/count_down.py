import time
import os


my_time = int(input('Enter the time in seconds: '))

for x in range(0, my_time):
  os.system('clear')
  print(x)
  time.sleep(1)
print('TIMES UP!')

for x in reversed(range(0, my_time)):
  os.system('clear')
  print(x)
  time.sleep(1)
print('TIMES UP!')
my_time = int(input("Enter the time is seconds: "))

for x in range(my_time, 0, -1):
  #os.system('clear')
  seconds = x % 60
  minutes = int(x / 60) % 60
  hours = int(x / 3600) 
  time.sleep(1)
  print(f'{hours}:{minutes:02}:{seconds:02}')
print('TIMES UP!')
