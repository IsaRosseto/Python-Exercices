# Exercício 1: Verificar Matriz Identidade
# Escreva um programa que receba uma matriz quadrada e verifique se ela é uma matriz identidade. 
#Uma matriz identidade é uma matriz quadrada em que todos os elementos da diagonal principal 
#são iguais a 1 e todos os outros elementos são iguais a 0.

def verifica_identidade(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        return False

    for i in range(linhas):
        for j in range(colunas):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False

    return True


# Exemplo de uso:
matriz1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matriz2 = [[1, 0, 0], [0, 1, 2], [0, 0, 1]]
print(verifica_identidade(matriz1))  # True
print(verifica_identidade(matriz2))  # False
