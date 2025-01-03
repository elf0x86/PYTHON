# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   iner loop:

# WHILE inside WHILE 
x = 10
y = 3
while x > 0:
  while y > 0:
    print(f'{x} - {y}')
    y -= 1
  x -= 1
  y = 3

# WHILE inside FOR
m = 10
for l in range(3):
  while m > 0:
    print(f'{l} - {m}')
    m -= 1
  m = 10
  
# FOR inside FOR
for i in range(3):
  for j in range(10):
    print(f'{i} - {j}')

# FOR inside WHILE
z = 10
while z > 0:
  for x in range(9):
    print(f'{z} - {x}')
  z -= 1

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
symbol = input('Enter a symbol to use: ')

for x in range(rows):
  for y in range(columns):
    print(symbol, end='')
  print()
