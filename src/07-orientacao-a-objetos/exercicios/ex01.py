class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, dados):
        """Cria um Aluno a partir de uma string no formato: prontuario,nome,email"""
        partes = dados.split(',')
        return cls(partes[0], partes[1], partes[2])

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Prontuário não pode ser vazio ou nulo")
        self._prontuario = valor.strip()

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Nome não pode ser vazio ou nulo")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Email não pode ser vazio ou nulo")
        self._email = valor.strip()

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.prontuario == other.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)


if __name__ == "__main__":
    aluno1 = Aluno.from_string("SP0101,João da Silva,joao@email.com")
    print(aluno1.prontuario)
    print(aluno1.nome)
    print(aluno1.email)

    aluno2 = Aluno("SP0102", "Maria Santos", "maria@email.com")

    print(aluno1 == aluno2)  # Falso
