def imprime_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if( j == colunas - 1 ):
                print('%d' %matriz[i][j])
            else:
                print('%d' %matriz[i][j], end=' ')
    print()