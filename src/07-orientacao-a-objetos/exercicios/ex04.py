from ex01 import Aluno


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    @classmethod
    def from_string(cls, dados):
        """Cria um Projeto a partir de uma string no formato: codigo,titulo,responsavel"""
        partes = dados.split(',')
        return cls(partes[0], partes[1], partes[2])

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or valor == '':
            raise ValueError("Código não pode ser vazio ou nulo")
        self._codigo = int(valor)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Título não pode ser vazio ou nulo")
        self._titulo = valor.strip()

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if not valor or not valor.strip():
            raise ValueError("Responsável não pode ser vazio ou nulo")
        self._responsavel = valor.strip()

    def add_participacao(self, participacao):
        """Adiciona uma participação ao projeto."""
        self.participacoes.append(participacao)

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False


if __name__ == "__main__":
    projeto = Projeto(1, "Laboratório Teste", "Pedro Gomes")

    aluno1 = Aluno("SP0101", "João da Silva", "joao@email.com")
    aluno2 = Aluno("SP0102", "Maria Santos", "maria@email.com")

    participacao1 = Participacao(
        1, "2025-03-01", "2025-06-30", aluno1, projeto)
    participacao2 = Participacao(
        2, "2025-04-01", "2025-07-31", aluno2, projeto)

    projeto.add_participacao(participacao1)
    projeto.add_participacao(participacao2)

    print(f"Projeto: {projeto.titulo}")
    print(f"Total de participações: {len(projeto.participacoes)}")

    for i, p in enumerate(projeto.participacoes, 1):
        print(f"{i}. {p.aluno.nome} - {p.data_inicio} a {p.data_fim}")
