# Variable = A container for a value (String, integer, float, boolean)
#            A variable behave as if it was the value it contains

# -- strings -------------
first_name = 'Lindomar'
food = 'Pizza'
email = 'test@mail.com'

print("first_name")
print(first_name)

# f-string
print(f'Hello {first_name}')
print(f'You like {food}')
print(f'Your email is: {email}')

# -- integers -------------
age = 25
quantity = 3
num_of_students = 30

print(f'You are {age} years old')
print(f'You are buying {quantity} items')
print(f'Your class has {num_of_students} students')

# -- float -------------
price = 10.99
great_point_average = 3.2
distance = 5.5

print(f'The price is ${price}')
print(f'Your gpa is: {great_point_average}')
print(f'You ran {distance}Km')

# -- boolean -------------
is_student = True # False
for_sale = False
is_online = True

print(f'Are you a student?: {is_student}')
if is_student:
  print('You are a student')
else:
  print('You are NOT a student')

if for_sale:
  print('That item is for sale')
else:
  print('That items is NOT available')

if is_onlie:
  print('You are online')
else:
  print('You are offline')





