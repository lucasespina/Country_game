import random
def sorteia_letra(palavra, negadas):
    especiais = ['.', ',', '-', ';', ' ']
    liberadas = []
    barradas = []

    # adicionar caracters especiais
    for items in especiais:
        negadas.append(items)

    # definir letras liberadas
    for letra in palavra:
        if letra == letra.upper():
            neutra = letra.lower()
        else:
            neutra = letra
        if neutra in negadas:
            barradas.append(letra)
        else:
            liberadas.append(letra)

    print(liberadas)

    if len(liberadas) != 0:
        escolhida = random.choice(liberadas)
        escolhida = escolhida.lower()
        return escolhida
    else:
        return ''