friends = 0

# increment variable
friends = friends + 1
print(friends) # 1
friends += 1
print(friends) # 2

# decrement variable
friends = friends - 2
friends -= 2

# multiplication
friends = 5
friends = friends * 3
friends *= 3

# division
friends = friends / 2
friends /= 2

# exponents
friends = friends ** 2
friends **= 2

# modules
remainder = friends % 3

# builtin math function
x = 3.14
y = -4
Y = 4
z = 5

result = round(x)  # 3
result = abs(y)    # 4
result = pow(Y, 3) # 64
result = max(x, y, Y, z) # 5
result = min(x, y, Y, z) # -4

import math

a = 9
b = 9.9

print(math.pi) # 3.14159...
print(math.e)  # 2.718281..
result = math.sqrt(a) # 3
result = math.ceil(b) # 10
result = math.floor(b) # 9


# EXERCISE calculate a circumference of a circle Fomula is c = 2*pi*r
radius = float(input('Enter the radius of a circle'))
circumference = 2 * math.pi * radius
print(f'The circumference is : {round(circumference, 2)}cm')
                    
# EXERCISE calculate the area of a circle Formula is a = pi*r
radius = float(input('Enter the radius of a circle: '))
area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)}cm²')

# EXERCISE calculate the hipotenuse of a right triangle formula is c = sqrt(a¹+b²)
a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = math .sqrt(pow(a, 2) + pow(b, 2))
print(f'Side c  = {c}')
