# for loops = execute a block o code a fixed number of time
#             You can iterate over a range, string, sequence, etc

for x in range(1,11):
  print(x)
print('HAPPY NEW YEAR!')

for i in reversed(range(1, 11)):
    print(i)
  print('HAPPY NEW YEAR!')

for r in range(11, 1, -1):
  print(r)
print('HAPPY NEW YEAR!')

for z in range(1, 11, 2):
  print(z)
print('HAPPY NEW YEAR!')

credit_card = '1234-4567-3459'
for x in credit_card:
  print(x)

for x in credit_card:
    print(x, end=f' --> {x*3}\n')
'''
1 --> 111
2 --> 222
3 --> 333
4 --> 444
- --> ---
4 --> 444
5 --> 555
6 --> 666
7 --> 777
- --> ---
3 --> 333
4 --> 444
5 --> 555
9 --> 999
'''

for x in range(1, 21):
  if x == 13:
    continue # skip an iteration
  else:
    print(x)


for x in range(1, 21):
  if x == 13:
    break
  else:
    print(x)


for x in range(1, 11):
   print(f'{x:>3} x 7 = {x * 7:-^10}', end=' ...\n')
'''
  1 x 7 = ----7----- ...
  2 x 7 = ----14---- ...
  3 x 7 = ----21---- ...
  4 x 7 = ----28---- ...
  5 x 7 = ----35---- ...
  6 x 7 = ----42---- ...
  7 x 7 = ----49---- ...
  8 x 7 = ----56---- ...
  9 x 7 = ----63---- ...
 10 x 7 = ----70---- ...
'''



