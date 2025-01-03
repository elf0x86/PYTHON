# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()
#               user input is alwas a string

name = 'Xamanta Eloquente'
age = 22
gpa = 3.1
is_student = True

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(is_student)) # <class 'bool'>


gpa = int(gpa)   # 3    <class 'int'>
age = float(age) # 22.0 <class 'float'>
age = str(age)   # '22' <class 'str'>

age =+ 1   # TypeError: can only concatenate str (not "int") to str
age += '9' # 22 + 9 = 299 string concatenation 

name = bool(name) # True
name = ''
name = bool(name) # False could be use to check if sombody type something or not
