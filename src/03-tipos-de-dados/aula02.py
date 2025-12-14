"""Aula 02 - Tipos de dados - Tuplas"""

# tupla
# ordenadas
# imutáveis
# indexadas

# criação da tupla
nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos (não é possivel por ser imutável)
# nomes[0] = 'Maria da Silva'

# iteração

for nome in nomes:
    print(nome)


for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'Ana', 'Amélia', 'Marcos'
print(nomes2, type(nomes2))

# unpack

# nome1 = nome2[0]
# nome2 = nome2[1]
# nome3 = nome2[2]

nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)

# juntar duas tuplas

todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))
