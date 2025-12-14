entrada = input('Digite as notas separadas por vírgula: ')

notas = [float(nota) for nota in entrada.split(',')]

media = sum(notas) / len(notas)

if media > 6.0:
    situacao = 'Aprovado'
elif media >= 4.0:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado'

print(f'\nMédia aritmética: {media:.2f}')
print(f'Situação: {situacao}')
