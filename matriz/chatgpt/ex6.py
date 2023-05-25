# Exercício 3: Verificar Matriz Simétrica
# Escreva um programa que receba uma matriz quadrada e verifique se ela é uma matriz simétrica.
# Uma matriz simétrica é aquela em que a transposta é igual à matriz original.

def verifica_simetrica(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        return False

    transposta = []
    for j in range(colunas):
        linha = []
        for i in range(linhas):
            linha.append(matriz[i][j])
        transposta.append(linha)

    return matriz == transposta


# Exemplo de uso:
matriz1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
matriz2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(verifica_simetrica(matriz1))  # True
print(verifica_simetrica(matriz2))  # False
