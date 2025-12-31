class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

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

    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False


if __name__ == "__main__":
    projeto1 = Projeto.from_string(
        "1,Laboratório Teste,Pedro Gomes")
    print(projeto1.codigo)
    print(projeto1.titulo)
    print(projeto1.responsavel)

    projeto2 = Projeto(2, "Sistema Teste", "Ana Silva")

    print(projeto1 == projeto2)  # Falso
