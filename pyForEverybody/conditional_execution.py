# Comparison Operator
# < <= == >= > !=
x = int(input('Number (0-9): '))

if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or equal to 5')
if x != 6:
    print('Not equal to 6')

print('Finis')

# Nested Decisions
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All done')


# Two-way Decision
x = 4
if x > 2:
    print('Bigger')
else
    print('Not bigger')
print('All Done')

# Multi-way branch
x = 32
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


x = 1
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Somethig else') # This line of code never runs

if x < 2:
    print('Below 2')
elif x < 20:
    print('Below 20')
elif x < 10:
    print('Below 10') # this line of code never runs
else:
    print('Something else')

# Error detection
name = 'Bob'
try:
    name = int(name) + 1
except:
    print('This don\'t work')
print(name)
