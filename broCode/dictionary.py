# dictionary = A collection of {key:value} pairs
#              ordered and changeable. No duplicates

capital = {'USA':'Washington D.C',
           'India': 'New Delhi',
           'Chine': 'Beijing',
           'Russia': 'Moscow'}

#print(dir(capitals))
#print(help(capitals))

print(capitals.get('USA'))
print(capitals.get('India'))
print(capitals.get('Japan')) # None

if capitals.get('Japan'):
  print('That capital exists')
else
  print('That capital doesn\'t exist')

capitals.update({'Germany': 'Berlin'})
print(capitals)

capitals.update({'USA': 'Detroit'})
capitals.pop('China')

capitals.popitem() # remove the latest element
capitals.clear()
capitals.key() # get all the keys
capitals.values() # get all values

for key in capitals.keys():
  print(key)

for value in capitals.values():
  print(value)


items = capitals.items() 
print(items)

for key, value in capitals.items():
  print(f'{key} --> {value}')

