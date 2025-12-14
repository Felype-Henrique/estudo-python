""" Conversão de tipos """

# Conversão implicita

leitura = 5.53
peso = 3
total = leitura * peso
print(total, type(total))

# Conversão explicita (type casting)

soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = 'Maria'
altura = 1.70

# mensagem = nome + 'tem a altura de ' + str(altura)
mensagem = f'{nome} tem a altura de {altura}'
print(mensagem)
