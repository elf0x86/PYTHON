print('-' * 30)
print('   CURSO EM VIDEO    ')
print('-' * 30)
print('   APRENDA PYTHON    ')
print('-' * 30)
print('   GUSTAVO GNUBARA   ')
print('-' * 30)

# Declarar função
def linhas():
    print('-' * 30)

linhas() # Chamar função para executar
print('   CURSO EM VIDEO    ')
linhas()
print('   APRENDA PYTHON    ')
linhas()
print('   GUSTAVO GNUBARA   ')
linhas()

def mensagem(msg):
    print('-----------------------------')
    print(msg)
    print('-----------------------------')

mensagem('    APRENDENDO ALGORITMOS   ')
mensagem('    APRENDENDO COMPILADOR   ')
mensagem('    APRENDENDO ASSEMBLER    ')

def titulo(txt):
    comp = int(len(txt)+10)
    print('-' * comp)
    print(f'{txt: ^{comp}}')
    print('-' * comp)

# Programa principal
titulo('meu titulo é chamativo')
titulo('O rato roeu a roupa do resto do rabo')


def myMsg(msg, linha_cima, linha_baixo):
    comp = int(len(msg)+10)
    if linha_cima == 1:
        print('=' * comp)
    print(f'{msg: ^{comp}}')
    if linha_baixo == 1:
        print('=' * comp)

myMsg('USAR LINUX É BACANA', 0, 1)
myMsg('USAR WINDOWS É PLAYBOY', 0, 1)



def soma(a, b):
    tot = a + b
    print(f'O total foi de: {tot:.2f}')

soma(3.321, 5.34)
soma(6, 3)
soma(a=2, b=8)
soma(b=8, a=2) # TROCAR A ORDEM DOS PARAMETROS È PERMITIDO


# PARAMETROS POR PADRÃO
print('PARAMETROS POR PADRÃO')
def soma2(a=566, b=100):
    tot = a + b
    print(f'O total foi de: {tot:.2f}')

soma2()
soma2(a=2, b=8)



# PASSAGEM DE PARAMETROS É PASSADA POR REFERENCIA
# DIFERENTE DO C, JAVA ONDE A PASSAGEM É POR VALOR
def dobra(lst): # TUDO QUE FOR MODIFICADO EM lst VAI MODIFICAR EM valores
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6,3,9,1,0,2]
print(valores)
dobra(valores)
print(valores)
print('-' * 40)

def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(5,2)
soma2(3,2,5,8)
print('-' * 40)
