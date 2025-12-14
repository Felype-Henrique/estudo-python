def calcular_imc(individuo):
    altura = individuo['altura']
    peso = individuo['peso']
    return peso / (altura * altura)


def obter_classificacao(imc):
    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25.0:
        return "Peso normal"
    elif imc < 30.0:
        return "Excesso de peso"
    elif imc < 35.0:
        return "Obesidade de Classe 1"
    elif imc < 40.0:
        return "Obesidade de Classe 2"
    else:
        return "Obesidade de Classe 3"


def situacao_individuo(imc):
    if imc < 18.5:
        return "ganhar peso"
    elif imc < 25.0:
        return "normal"
    else:
        return "perder peso"


peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

individuo = {
    'altura': altura,
    'peso': peso
}

imc = calcular_imc(individuo)
classificacao = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print(f"\nIMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Situação: {situacao}")
