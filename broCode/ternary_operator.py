# conditional expression
# A one-line shortcut for the if-else statement
# print or assign one of two values based on a condition
# x if condition else y

num = 5
print('positive' if num > 0 else 'negative')

result = 'even' if num % 2 == 0 else 'odd'
print(result)

a = 6
b = 7
max_num = a if a > b else b # b=7
min_num = a if a < b else b # a=6

age = 26
status = 'Adult' if age >= 18 else 'Child'

temperature = 30
weather = 'HOT' if temperature > 20 else 'COLD'

user_role = 'admin' # Guest
acess_level = 'Full access' if user_role == 'admin' else 'Limited acces'

