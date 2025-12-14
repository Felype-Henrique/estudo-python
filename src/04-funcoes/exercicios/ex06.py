def calcular_volume(medidas):
    comprimento = medidas['comprimento']
    altura = medidas['altura']
    largura = medidas['largura']
    return (comprimento * altura * largura) / 1000


def calcular_potencia_termostato(volume, temperaturas):
    temp_desejada = temperaturas['temp_desejada']
    temp_ambiente = temperaturas['temp_ambiente']
    return volume * 0.05 * (temp_desejada - temp_ambiente)


def calcular_filtragem(volume):
    filtragem_minima = volume * 2
    filtragem_maxima = volume * 3
    return filtragem_minima, filtragem_maxima


comprimento = float(input("Digite o comprimento do aquário (cm): "))
altura = float(input("Digite a altura do aquário (cm): "))
largura = float(input("Digite a largura do aquário (cm): "))
temp_desejada = float(input("Digite a temperatura desejada (°C): "))
temp_ambiente = float(input("Digite a temperatura ambiente (°C): "))

medidas = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura
}

temperaturas = {
    'temp_desejada': temp_desejada,
    'temp_ambiente': temp_ambiente
}

volume = calcular_volume(medidas)
potencia = calcular_potencia_termostato(volume, temperaturas)
filtragem_min, filtragem_max = calcular_filtragem(volume)

print(f"\nVolume: {volume:.2f} litros")
print(f"Potência do termostato: {potencia:.2f} watts")
print(f"Filtragem: {filtragem_min:.2f} a {filtragem_max:.2f} litros/hora")
