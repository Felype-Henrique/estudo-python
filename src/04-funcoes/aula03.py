"""Aula 03 -  *args e **kwargs"""


def world_cup_titles(country, *args):
    print(f'Country: {country}')
    for title in args:
        print(f'Year: {title}')
    print()


print("\n1. Brasil com 5 títulos:")
world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

print("2. Espanha com 1 título:")
world_cup_titles('Espanha', '2010')

print("3. Alemanha com 4 títulos:")
world_cup_titles('Alemanha', '1954', '1974', '1990', '2014')

print("4. França com 2 títulos:")
world_cup_titles('França', '1998', '2018')


def soma_numeros(*args):
    total = sum(args)
    print(f"Números: {args}")
    print(f"Soma: {total}")
    return total


def concatenar_palavras(separador, *args):
    resultado = separador.join(args)
    print(f"Resultado: {resultado}")
    return resultado


print("\n2. Separando com hífen:")
concatenar_palavras('-', 'Brasil', 'Campeão', 'Mundial')

print("\n3. Separando com vírgula:")
concatenar_palavras(', ', 'Maçã', 'Banana', 'Laranja', 'Uva')


def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')

    print(f"\nValor base: R$ {value:.2f}")

    if tax_percentage:
        tax_value = value * (tax_percentage / 100)
        value += tax_value
        print(f"Imposto ({tax_percentage}%): R$ {tax_value:.2f}")

    if discount:
        value -= discount
        print(f"Desconto: R$ {discount:.2f}")

    print(f"Valor final: R$ {value:.2f}")
    return value


print("\n1. Preço sem desconto ou impostos:")
final_price = calculate_price(100.0)

print("\n2. Preço com desconto de R$ 5:")
final_price = calculate_price(100.0, discount=5.0)

print("\n3. Preço com imposto de 7%:")
final_price = calculate_price(100.0, tax_percentage=7)

print("\n4. Preço com imposto de 7% e desconto de R$ 5:")
final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
