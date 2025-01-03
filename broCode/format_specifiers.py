# Format specifiers = {value:flags} format a value based on what
#                                   flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that may spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# :  = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator each THOUSANDS place is separeted with a comma

price1 = 3.14159
price2 = -986.6523
price3 = 12.3425

print('\n.(number)f = round to that many decimal places (fixed point)')
print(f'Price 1 is ${price1:.2f}')
print(f'Price 2 is ${price2:.2f}')
print(f'Price 3 is ${price3:.2f}')
print(f'Price 1 is ${price1:.1f}')
print(f'Price 2 is ${price2:.1f}')
print(f'Price 3 is ${price3:.1f}')

print('\n:(number) = allocate that many spaces')
print(f'Price 1 is ${price1:10}')
print(f'Price 2 is ${price2:10f}')
print(f'Price 3 is ${price3:10f}')
print(':03 = allocate and zero pad that may spaces')
print(f'Price 1 is ${price1:010}')
print(f'Price 2 is ${price2:010f}')
print(f'Price 3 is ${price3:010f}')

print('\n:< = left justify')
print(f'Price 1 is ${price1:<10}')
print(f'Price 2 is ${price2:<10}')
print(f'Price 3 is ${price3:<10}')

print('\n:> = right justify')
print(f'Price 1 is ${price1:>10}')
print(f'Price 2 is ${price2:>10}')
print(f'Price 3 is ${price3:>10}')

print('\n:^ = center align')
print(f'Price 1 is ${price1:^20}')
print(f'Price 2 is ${price2:^20}')
print(f'Price 3 is ${price3:^20}')

print('\n:-^ = symbol center align')
print(f'Price 1 is ${price1:-^20}')
print(f'Price 2 is ${price2:-^20}')
print(f'Price 3 is ${price3:-^20}')

print('\n:+ use a plus sign to indicate positive value')
print(f'Price 1 is ${price1:+}')
print(f'Price 2 is ${price2:+}')
print(f'Price 3 is ${price3:+}')

print('\n:+20 use a plus sign to indicate positive value and a number to justify')
print(f'Price 1 is ${price1:+20}')
print(f'Price 2 is ${price2:+20}')
print(f'Price 3 is ${price3:+20}')

print('\nCombination of flags')
price1 = 36766.14159
price2 = -9865125.6523
price3 = 12234.3425
print(f'Price 1 is ${price1:+,.2f}')
print(f'Price 2 is ${price2:+,.2f}')
print(f'Price 3 is ${price3:+,.2f}')










