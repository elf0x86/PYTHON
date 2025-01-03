# Pound to Kilograms or Kilograms to Pounds

weight = float(input('Enter you weight: '))
unit   = input('Kilograms or Pounds (K or L): ').upper()

if unit == 'K':
  weight = weight * 2.205
  unit = 'Lbs'
elif unit == 'L':
  weight = weight / 2.205
  unit = 'Kgs'
else:
  print(f'{unit} was not valid')

print(f'Your weight is: {round(weight, 2)v} {unit}')


