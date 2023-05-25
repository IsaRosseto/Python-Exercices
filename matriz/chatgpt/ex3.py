# Exercício 3: Transposição de Matriz
# Escreva um programa que receba uma matriz e retorne sua transposta.

def transpor_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    matriz_transposta = []

    for j in range(colunas):
        linha = []
        for i in range(linhas):
            linha.append(matriz[i][j])
        matriz_transposta.append(linha)

    return matriz_transposta


# Exemplo de uso:
matriz = [[1, 2, 3], [4, 5, 6]]
resultado = transpor_matriz(matriz)
print(resultado)
