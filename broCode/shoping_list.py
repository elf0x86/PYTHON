foods = list()
price = list()
total = 0

while True:
  food = input('Enter a food to buy (q to quit): ').lower()
  if food == 'q':
    break
  else:
    price = float(input(f'Enter the price of {food} $: '))
    foods.append(food)
    prices.append(price)

print('----- YOUR CART -----')
for food in foods:
  print(f'{food}', end=' ')
for price in prices:
  total += price
  
print(f'Your total is ${total}') 
    
