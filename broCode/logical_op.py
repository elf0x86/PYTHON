# Logical operators = evaluate multiple conditions (or , and, not)
#                     or = at least one condition must be True
#                     and = both condition must be True
#                     not = inverts the condition ( not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or tem is_rainig:
  print('The outdoor event is cancelled')
else:
  print('The outdoor event is still scheduled')


temp = int(input('What is the temperature outside: '))
is_sunny = input('It is Sunny or Cloudy outside? (S/C): ').upper()

is_sunny = True if is_sunny == 'S' else False

if temp >= 28 and is_sunny:
  print('It is HOT outside 🥵')
  print('It is SUNNY ☀️')
elif temp <= 0 and is_sunny:
  print('It is cold outside 🥶')
  print('It is SUNNY ☀️')
elif temp < 28 and temp > 0 and is_sunny:
  print('It is WARM outside 🙂')
  print('It is SUNNY ☀️')

elif temp >= 28 and not is_sunny:
  print('It is HOT outside 🥵')
  print('It is CLOUDY ☁️ ')
elif temp <= 0 and  not is_sunny:
  print('It is cold outside 🥶')
  print('It is CLOUDY ☁️')
elif temp < 28 and temp > 0 and  not is_sunny:
  print('It is WARM outside 🙂')
  print('It is CLOUDY ☁️')

