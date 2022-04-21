def calcula_dimensoes(matriz):
    altura = len(matriz)
    largura = 1
    for item in matriz:
        largura = len(item)
        break
    return '{}'.format(altura) + 'X' + '{}'.format(largura)


def dimensoes(matriz):
    print(calcula_dimensoes(matriz))
