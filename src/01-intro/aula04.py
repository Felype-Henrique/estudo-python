""" Aula 04 - Variáveis , Constantes e Literais"""

# Variavel  container para guardar dados
# inferencia de tipo
numero = 10
print(numero, type(numero))

# alterar o valor da variavel
numero = 20
print(numero)

# multiplas atribuições
nome, idade, endereco = 'Maria', 30, 'Rua das ...'
print(nome, idade, endereco)


nome = 'Maria'
idade = 30
endereco = 'Rua das ...'

print(nome, idade, endereco)

# atribui o mesmo valor para varias variaveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# snake_case
id_funcionario = 209
salario_atual = 5000.50
print(id_funcionario, salario_atual)

# Constantes
# Upper case - snake case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)


# Literais
idade = 27
print(idade)
print(27)

# Númericos
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))


# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("John's house")
print('O filme estava "excelente"')


# Boolean
print(True, type(True))
print(False, type(False))


# None
print(None, type(None))

# Coleções

# Listas (list)
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tuplas (tuple)
email = ('joao@email.com', 'maria@email.com')
print(email, type(email))

# Conjuntos (set)
nomes = {'Maria', 'João', 'Pedro', 'Maria'}
print(nomes, type(nomes))

# Dicionários
alunos = {
    'prontuario': 123456,
    'nome': 'Maria da Silva',
    'idade': 34
}

print(alunos, type(alunos))
