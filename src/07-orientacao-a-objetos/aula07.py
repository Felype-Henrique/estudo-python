"""Aula 07 - Relacionamento entre classes"""


class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep={self.cep}, numero={self.numero}]'


class Telefone:

    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'


class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'


telefone = Telefone('11', '1111-1111')
pessoa1 = Pessoa('11233213', 'Joao da Silva',
                 telefone, Endereco('12345-678', 123))
pessoa1.add_endereco(Endereco('98765-432', 456))

pessoa2 = Pessoa('233213', 'Maria da Silva',
                 telefone, Endereco('54321-876', 789))

pessoa3 = Pessoa('99887766', 'Ana Paula', telefone, Endereco('54321-876', 719))

print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)

print(pessoa2)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
