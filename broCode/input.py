# input() = A function that prompts the user to enter data
#           Returns the entered data as a string
# All user input are string

input('What is your name?: ') # the result was not saved anywhere
name = input('What is your name?: ')
# age = input('How old are you?: ')

# consdense the type casting
age = int(input('How old are you?: '))


# age = age + 1 # TypeError: can only concatenate str (not 'int') to str
# age = int(age)
age = age + 1

print(f'Hello {name}!')
print('HAPPY BIRTHDAY!')
print(f'You are {age} years old!')


# exercise 1 Rectangle Area Calc
length = int(input('Enter the length: '))
width  = int(input('Enter the width: '))
area = length * width
print(f'The area is: {area}cm²')


# exercise 2 Shopping car problem
item = input('What item would you like to buy?: ')
price = float(input('What is the price?: '))
quantity = int(input('How many would you like?: '))
total = price * quantity
print(f'You have bought {quantity}  x {items}/s')
print(f'Your total is ${total')



