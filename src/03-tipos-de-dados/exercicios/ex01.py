numeros = []

numero1 = float(input('Digite o primeiro número: '))
numeros.append(numero1)

numero2 = float(input('Digite o segundo número: '))
numeros.append(numero2)

numero3 = float(input('Digite o terceiro número: '))
numeros.append(numero3)

menor = min(numeros)
maior = max(numeros)

print(f'Menor elemento: {menor}')
print(f'Maior elemento: {maior}')
