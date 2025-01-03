# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must no contain digits

user_name = input('Enter your name: ')

if len(user_name) > 12:
  print('Your user name can\'t be more than 12 characters')
elif not user_name.find(' ') == -1:
  print('Your user name can\'t contain spaces')
elif not user_name.isalpha():
  print('Your user name can\'t contain numbers')
else:
  print(f'Welcome {user_name}')

