fruits =     ['apple',  'orange',   'banan',    'coconut']
vegetables = ['celery', 'carrots',  'potatoes', 'tomatos']
meats =      ['chiken', 'fish',     'turkey',    'beaf']

groceries = [fruits, vegetables, meats]

# 2D-List of List
groceries2 = [['apple',  'orange',   'banan',    'coconut'],
              ['celery', 'carrots',  'potatoes', 'tomatos'],
              ['chiken', 'fish',     'turkey',    'beaf']]

# Tuple of Tuple
groceries3 = (('apple',  'orange',   'banan',    'coconut'),
              ('celery', 'carrots',  'potatoes', 'tomatos'),
              ('chiken', 'fish',     'turkey',    'beaf'))

# List of Tuple
groceries4 = [('apple',  'orange',   'banan',    'coconut'),
              ('celery', 'carrots',  'potatoes', 'tomatos'),
              ('chiken', 'fish',     'turkey',    'beaf')]

# Tuple of Sets
groceries5 = ({'apple',  'orange',   'banan',    'coconut'},
              {'celery', 'carrots',  'potatoes', 'tomatos'},
              {'chiken', 'fish',     'turkey',    'beaf'})
# Set of Tuples
groceries6 = {('apple',  'orange',   'banan',    'coconut'),
              ('celery', 'carrots',  'potatoes', 'tomatos'),
              ('chiken', 'fish',     'turkey',    'beaf')}

print(groceries[0][0]) # apple

for collection in groceries:
    print(collection)
    for food in collection:
      print(food, end=' ')
    print()

# 2D-tuple
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ('*', 0, '#'))

for row in num_pad:
  for num in row:
    print(num, end=' ')
  print()



