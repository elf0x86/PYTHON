print(f"soma      = {3 + 5}")
print(f"subt      = {10 - 7}")
print(f"mult      = {5 * 3}")
print(f"divi      = {20 / 3}")
print(f"pote      = {2**8}")
print(f"divi_int  = {20 / 3}")
print(f"resto_div = {20 % 3}")
print('='*5)
print("repeat\n" * 3)
print('='*5)


# Ordem de Precedência dos operadores
# 1 ()
# 2 **
# 3 * / // %
# 4 + -


exe01 = 5 + 3 * 2        # 11
exe02 = 3 * 5 + 4 ** 2   # 31
exe03 = 3 * (5 + 4) ** 2 # 243

print(f"exe01 = {exe01}")
print(f"exe02 = {exe02}")
print(f"exe03 = {exe03}")

# Função interna
print(pow(2,8))

# Função externa
import math
print(81**(1/2)) # raiz quadrada
print(math.sqrt(81))
