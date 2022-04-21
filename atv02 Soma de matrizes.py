def calcula_dimensoes(matriz):
    altura = len(matriz)
    largura = 1
    for item in matriz:
        largura = len(item)
        break
    return altura, largura


def soma_matrizes(m1, m2):
    a, l = calcula_dimensoes(m1)
    if calcula_dimensoes(m1) != calcula_dimensoes(m2):
        return False
    else:
        m3 = m1
        for i in range(0, a):
            for j in range(0, l):
                m3[i][j] = m1[i][j] + m2[i][j]
    return m3