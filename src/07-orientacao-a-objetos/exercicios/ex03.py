from ex01 import Aluno
from ex02 import Projeto


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto


if __name__ == "__main__":
    aluno = Aluno.from_string("SP0101,João da Silva,joao@email.com")
    projeto = Projeto.from_string("1,Lab Teste,Pedro Gomes")

    participacao = Participacao(
        codigo=1,
        data_inicio="2025-03-01",
        data_fim="2025-06-30",
        aluno=aluno,
        projeto=projeto
    )

    print(f"Código: {participacao.codigo}")
    print(f"Período: {participacao.data_inicio} até {participacao.data_fim}")
    print(f"Aluno: {participacao.aluno.nome}")
    print(f"Projeto: {participacao.projeto.titulo}")
