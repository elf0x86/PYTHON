# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = '1234-5678-9012-3456'
print(credit_number[0]) # 1
print(credit_number[1]) # 2
print(credit_number[0:4]) # 1234
print(credit_number[5:9]) # 5678
print(credit_number[5:])  # 5678-9012-3456
print(credit_number[-1])  # 6
print(credit_number[-2])  # 5
print(credit_number[-3])  # 4
print(credit_number[::2]) # 13-6891-46
print(credit_number[::3]) # 146-136

last_4_digit = credit_number[-4:]
print(f'XXXX-XXXX-XXXX-{last_4_digit}')

# REVERSE THE STRING
print(credit_number[::-1])


