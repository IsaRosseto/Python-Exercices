# Exercício 2: Obter Diagonal Principal
# Escreva um programa que receba uma matriz quadrada e retorne uma lista com os elementos da diagonal principal.

def obter_diagonal_principal(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        return None

    diagonal = []
    for i in range(linhas):
        diagonal.append(matriz[i][i])

    return diagonal


# Exemplo de uso:
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = obter_diagonal_principal(matriz)
print(resultado)  # [1, 5, 9]

