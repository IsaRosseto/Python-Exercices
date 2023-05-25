# Crie uma matriz m[12][12] com números inteiros aleatórios(de 0 até 99, randint(0, 99)). Em seguida, calcule e mostre a soma considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo(área verde).
# a area verde é um triangulo que inicia na linha 7 coluna 5 e 6 e termina na linha 11 na coluna da 1 a 10


import random


# Criação da matriz
matriz = [[random.randint(0, 99) for _ in range(12)] for _ in range(12)]

# Cálculo da soma dos elementos da área inferior (triângulo verde)
soma = 0
for i in range(7, 12):
    for j in range(12-i, i+1):
        soma += matriz[i][j]

# Impressão da matriz e da soma
for linha in matriz:
    print(linha)

print("Soma da área inferior:", soma)

# Neste código, utilizamos a função random.randint(0, 99) para gerar números inteiros aleatórios no intervalo de 0 a 99. A matriz m é criada como uma lista de listas, com dimensões 12x12.

# Em seguida, percorremos a área inferior do triângulo verde dentro da matriz, que inicia na linha 7 e coluna 5 (índices 6 e 4 respectivamente) e termina na linha 11 (índice 10) com as colunas variando de 1 a 10 (índices 0 a 9). Somamos os valores dos elementos dessa área à medida que percorremos a matriz.

# Por fim, imprimimos a matriz gerada e a soma dos elementos da área inferior conforme solicitado.
