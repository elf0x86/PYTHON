operator = input('Enter an operator (+ - * /): ')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))


if operator == '+':
  result = num1 + num2
  print(f'{num1} + {num2} = {round(result, 2)}')
elif operator == '-':
  result = num1 - num2
  print(f'{num1} - {num2} = {round(result, 2)}')
elif operator == '*':
  result = num1 * num2
  print(f'{num1} x {num2} = {round(result, 2)}')
elif operator == '/':
  result = num1 / num2
  print(f'{num1} / {num2} = {round(result, 2)}')
else:
  print(f'Invalid Operator <{operator}>')







