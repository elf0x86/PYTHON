# collection = single 'variable' used to store multiple values
#  List  = [] ordered and changeable. Duplicates Ok
#  Set   = {} unordered and immutable, but ADD/REMOVE Ok. No Duplication
#  Tuple = () ordered and unchangeble. Duplicate Ok. Faster than lists

fruits = ['apple', 'orange', 'banana', 'coconut']
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[4]) # IndexError: list index out of range

print(fruits[0:3]) # apple orange banana
print(fruits[::2]) # apple banana
print(fruits[::-1]) # coconut banana orange apple

for fruit in fruits:
  print(fruit)

dir(fruits) # list all methods this object have
help(fruits) # list the help for each method

print(len(fruits))

print('apple' in fruits)     # True
print('pineapple' in fruits) # False

fruits[0] = 'pineapple'
fruits.append('mango') # append in the end of the list
fruits.remove('apple') # remove element from the list
fruits.insert(3, 'bbary') # insert an element in a given index
fruits.sort() # sort in alphabetical order
fruits.revers() # reverse alist base in the original order
fruits.sort().reverse()
fruits.clear() # all the elements are gone
fruits.index('apple')
fruits.count('banana') # count the total of elements in a list


# Set works well if you are working with constants like colors
fruits = {'apple', 'orange', 'banana', 'coconut', 'coconut'}
print(dir(fruits))
print(len(fruits))
print('banana' in fruits)
print(fruits[0]) # TypeError: set object is not subscriptable
fruits.add('pineapple')
fruits.remove('banana')
fruits.pop() # removes the first object (it is random)
fruits.clear() 


# Tuple faster than list
fruits = ('apple', 'orange', 'banana', 'coconut', 'coconut')
print(dir(fruits))
print(len(fruits))
print(help(fruits))
print('banana' in fruits)
print(fruits.index('apple')) # 0
print(fruits.count('coconuts')) # 2

for fruit in fruits:
  print(fruit)













