# Exercício 2: Multiplicação de Matrizes
# Escreva um programa que receba duas matrizes e retorne a matriz resultante da multiplicação entre elas.

def multiplica_matrizes(matriz1, matriz2):
    linhas1 = len(matriz1)
    colunas1 = len(matriz1[0])
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    if colunas1 != linhas2:
        return None

    matriz_resultante = []
    for i in range(linhas1):
        linha = []
        for j in range(colunas2):
            soma = 0
            for k in range(colunas1):
                soma += matriz1[i][k] * matriz2[k][j]
            linha.append(soma)
        matriz_resultante.append(linha)

    return matriz_resultante


# Exemplo de uso:
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
resultado = multiplica_matrizes(matriz1, matriz2)
print(resultado)
