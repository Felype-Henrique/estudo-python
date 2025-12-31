""" Aula 01 - Debug """


def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma


def calcular_media(nota1, nota2, nota3):
    media = somar(nota1, nota2, nota3)
    media = media / 3
    return media


nota1 = 10.0
nota2 = 3.0
nota3 = 5.5

media = calcular_media(nota1, nota2, nota3)
print(media)
