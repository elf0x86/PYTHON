# if - Do some code only IF some condition id True
#      Else do something else

age = int(input('Enter your age: '))
if age >= 18:
  print(f'You are now signed up!')
elif age < 0:
  print(f'You havent been bonr yet!')
elif age >= 100:
  print(f'You are too old to sign up!')
else:
  print(f'You must be 18+ to sign up!')

# ATENTION with the order of if elif statement
if age >= 100:
  print(f'You are too old to sign up!')
elif age >= 18:
  print(f'You are now signed up!')
elif age < 0:
  print(f'You havent been bonr yet!')
else:
  print(f'You must be 18+ to sign up!')

response = input('Would you like food? (Y/N): ')
if response == 'Y':
  print('Have some food!')
else response == 'N':
  print('No food for you!')


name = input('Enter your name: ')
if name == '':
  print('You did not type in your name!')
else:
  print(f'Hello {name}!')


for_sale = True
if for_sale:
  print('This item is for sale')
else:
  print('This item is NOT for sale')

online = True
if online:
  print('The user is online')
else:
  print('The user is offline')

