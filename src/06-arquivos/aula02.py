""" Aula 02 - Manipulando Arquivos com Python """

# arq = open('arquivo.txt', 'w')

# x = ['Caio\n', 'João\n', 'Marcos\n']

# arq.writelines(x)

# arq.close()

with open('src/06-arquivos/arquivo.txt', 'r') as arq:
    x = arq. readlines()
    print(type(x))

with open('src/06-arquivos/arquivo.txt', 'rb') as arq:
    x = arq. read()
    print(type(x))
    print(x.decode())

with open('src/06-arquivos/arquivo.txt') as arq:
    print(next(arq))
    print(next(arq))
