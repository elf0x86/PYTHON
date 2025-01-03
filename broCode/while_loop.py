# while loop = execute some code WHILE some condition remains true

name = input('Enter your name: ')
while name == '':
  print('You did not enter your name')
  name = input('Enter your name: ')
print(f'Hello {name}')

# Be carfull with infinite LOOP
name = ''
while name == '':
  print('You did not enter your name')

age = int(input('Enter your age: '))
whie age < 0:
  print('Age can\'t be negative')
  age = int(input('Enter your age: '))

food = input('Enter a food you like (q to quit): ').lower()
while not food == 'q':
  print(f'You like {fodd}')
  food = input('Enter another food you like (q to quit): ')
print(f'bye')

number int(input('Enter a number between 1 - 10: '))
while number < 1 or number > 10:
  number = int(input(f'{number} is not valide\nEnter a number 1 - 10: '))
print(f'Your number is {number}')

