"""  Aula 01 - Manipulando Arquivos"""

# open("caminho","r")

# Modes
# r - Leitura
# a - append / Incrementar
# w - Escrita
# x - Criar Arquivo
# r+ - Leitura e Escrita

# arquivo = open("src/06-arquivos/test.txt", "r")

# print(arquivo.read())
# print(arquivo.readable())
# print(arquivo.readlines())
# print(arquivo.readlines())
# print(arquivo.readlines())
# print(arquivo.readlines())

# lista = arquivo.readline()

# print(lista)

# print(lista[3])

# arquivo = open("src/06-arquivos/test2.txt", "w")


# arquivo.write("Python\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# arquivo.close


import os
# if os.path.exists("src/06-arquivos/test2.txt"):
#     os.remove("src/06-arquivos/test2.txt")
# else:
#     print("O arquivo não existe")

os.rmdir("src/06-arquivos/nova_pasta")
