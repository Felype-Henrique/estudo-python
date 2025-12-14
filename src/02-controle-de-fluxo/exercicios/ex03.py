identificador = input('Digite o identificador: ')

if len(identificador) == 7 and identificador[:2] == 'BR' and identificador[2:6].isdigit() and identificador[6] == 'X':
    numero = int(identificador[2:6])
    if 1 <= numero <= 9999:
        print('Identificador válido')
    else:
        print('Identificador inválido')
else:
    print('Identificador inválido')
