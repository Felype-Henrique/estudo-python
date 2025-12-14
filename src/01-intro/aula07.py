""" I/O Input e Output """

# saída padrão - sys stdout
print('Hello World!', 'Maria', 1, True, sep='@', end='!!!!!\n')
# print('Hello World!', 'Maria', 1, True, sep='@', end=' ')

arquivo = open('nomes.txt', 'w', encoding='utf8')

print('joao@email.com', 'maria@email.com',
      'pedro@email.com', file=arquivo, sep=';')


# Entrada

# nome = input('Qual seu nome?')
# idade = int(input('Qual sua idade?'))

# if idade >= 18:
#     print(f'{nome}, você é maior de idade')
# else:
#     print(f'{nome}, você é menor de idade')


# file

arquivo_notas = open('notas.txt', 'r', encoding='utf8')
conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
notas = [float(nota) for nota in notas]
print(notas)

media = ((notas[0]) + (notas[1]) + (notas[2])) / len(notas)
print(media)
