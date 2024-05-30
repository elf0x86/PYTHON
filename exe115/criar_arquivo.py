print(f'{"LENDO O ARQUIVO":=^40}')
try:
    # Abrir arquivo em modo leitura
    usuarios = open('data.txt', 'r')
    print(usuarios.read())
    usuarios.close()
#    print(usuarios.readline())

    # Abrir arquivo em modo inserção
    usuarios = open('data.txt', 'a')
    usuarios.write('THIS WILL BE INSERTED AT THE END\n')
    usuarios.close()

    # Abrir arquivo em modo leitura
    usuarios = open('data.txt', 'r')
    print(usuarios.read())
    usuarios.close()

#    conteudo = usuarios.read()
#    print(conteudo)


except FileNotFoundError:
    print(f'FileNotFoundError 0_o')


