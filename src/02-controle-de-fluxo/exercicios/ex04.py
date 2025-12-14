identificador = input('Digite o identificador: ')

erros = []

if len(identificador) != 7:
    erros.append('O identificador não contém 7 caracteres.')

if len(identificador) >= 2:
    if identificador[0:2] != 'BR':
        erros.append('O identificador não inicia com a sequência BR.')

if len(identificador) >= 6:
    if not identificador[2:6].isdigit():
        erros.append(
            'O identificador não apresenta número inteiro entre 0001 e 9999.')
    else:
        numero = int(identificador[2:6])
        if numero < 1 or numero > 9999:
            erros.append(
                'O identificador não apresenta número inteiro entre 0001 e 9999.')

if len(identificador) >= 7:
    if identificador[6] != 'X':
        erros.append('O identificador não finaliza com o caractere X.')

if len(erros) == 0:
    print('Identificador válido')
else:
    print('Identificador inválido')
    print('Erros:')
    for erro in erros:
        print(f'  - {erro}')
