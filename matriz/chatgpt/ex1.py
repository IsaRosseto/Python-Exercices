# Exercício 1: Soma de Matrizes
# Escreva um programa que receba duas matrizes de mesma dimensão e retorne a soma delas.

def soma_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    matriz_soma = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        matriz_soma.append(linha)

    return matriz_soma


# Exemplo de uso:
matriz1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
resultado = soma_matrizes(matriz1, matriz2)
print(resultado)
