def carregar_dados_projetos(nome_arquivo):
    """Retorna uma tupla de dicionários com dados de projetos."""
    lista_projetos = []

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()

            if linha:
                campos = linha.split(',')

                projeto = {
                    'codigo': int(campos[0]),
                    'titulo': campos[1],
                    'responsavel': campos[2]
                }

                lista_projetos.append(projeto)

    return tuple(lista_projetos)


projetos = carregar_dados_projetos('src/06-arquivos/exercicios/projetos.txt')
for projeto in projetos:
    print(projeto)
