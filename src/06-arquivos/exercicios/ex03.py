def linha_para_dict(linha, chaves):
    """Recebe uma linha e uma lista de chaves e retorna um dicionário."""
    linha = linha.strip()
    valores = linha.split(',')

    dicionario = {}
    for i, chave in enumerate(chaves):
        if i < len(valores):
            dicionario[chave] = valores[i]
        else:
            dicionario[chave] = ''

    return dicionario


if __name__ == "__main__":
    print("Exemplo 1:")
    linha1 = "SP000001,Maria da Silva,maria@email.com"
    chaves1 = ['prontuario', 'nome', 'email']
    resultado1 = linha_para_dict(linha1, chaves1)
    print(f"Linha: {linha1}")
    print(f"Chaves: {chaves1}")
    print(f"Saída: {resultado1}")

    print("\nExemplo 2:")
    linha2 = "banana,3"
    chaves2 = ['item', 'quantidade']
    resultado2 = linha_para_dict(linha2, chaves2)
    print(f"Linha: {linha2}")
    print(f"Chaves: {chaves2}")
    print(f"Saída: {resultado2}")
