def notas(* todas, sit=False):
    tmp_dict = dict()
    total = 0
    maior = 0
    menor = 0
    soma  = 0
    for x in range(0, len(todas)):
        total += 1

        if x == 0:
            maior = todas[x]
            menor = todas[x]

        if maior < todas[x]:
            maior = todas[x]

        if menor > todas[x]:
            menor = todas[x]

        soma += todas[x]
     
    tmp_dict['total'] = total 
    tmp_dict['maior'] = maior
    tmp_dict['menor'] = menor
    tmp_dict['media'] = soma / total

    if sit:
        if tmp_dict['media'] <= 6:
            tmp_dict['situação'] = 'RUIM'
        if tmp_dict['media'] > 6 and tmp_dict['situação'] < 7:
            tmp_dict['situação'] = 'BOA'
        if tmp_dict['media'] > 7 and tmp_dict['situação'] <= 9:
            tmp_dict['situação'] = 'OTIMA'
        if tmp_dict['media'] == 10:
            tmp_dict['situação'] = 'EXCELENTE' 

    print(todas, tmp_dict)

notas(1,3,5,6,7)
notas(1,3,5,6,7, sit=True)

print('=' * 100)

# SOLUÇÃO DO VIDEO -------------------------------------------------------------------
def notas (*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

# Programa Principal
resp = notas (5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
