def carregar_dados_alunos(nome_arquivo):
    """Retorna uma tupla de dicionários com dados de
alunos."""
    alunos = []

    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                partes = linha.split(',')

                aluno = {
                    'prontuario': partes[0],
                    'nome': partes[1],
                    'email': partes[2]
                }

                alunos.append(aluno)

    return tuple(alunos)


alunos = carregar_dados_alunos('src/06-arquivos/exercicios/alunos.txt')
for aluno in alunos:
    print(aluno)
