meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

numero_mes = int(input('Digite o número do mês (1-12): '))

if numero_mes >= 1 and numero_mes <= 12:
    print(f'Mês: {meses[numero_mes - 1]}')
else:
    print('Número inválido. Digite um valor entre 1 e 12.')
