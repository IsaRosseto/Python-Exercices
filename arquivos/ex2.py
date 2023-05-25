# Exercício 2
# • Escreva uma função em Python para retornar a somatória de todos os
# números que estão armazenados no arquivo “numeros2.txt”.
# • Todos os números do arquivo estão na mesma e única linha, separados
# por espaço.

# Ler a linha do arquivo "numeros2.txt" e armazená-la em uma string
with open("numeros2.txt", "r") as arquivo_numeros:
    linha = arquivo_numeros.readline()

# Separar a string em números individuais
numeros = linha.split()

# Converter cada número em um inteiro e calcular a soma
soma = sum(int(numero) for numero in numeros)

# Exibir o resultado
print("A soma dos números é:", soma)
