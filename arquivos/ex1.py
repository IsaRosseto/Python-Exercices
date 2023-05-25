# Exercício 1
# • Crie um programa que inverta a ordem das linhas do arquivo pares.txt.
# • A primeira linha deve conter o maior número e a última linha o menor.
# • Salve o resultado em outro arquivo(invertido.txt).

# Ler as linhas do arquivo "pares.txt" e armazená-las em uma lista
with open("pares.txt", "r") as arquivo_pares:
    linhas = arquivo_pares.readlines()

# Inverter a ordem da lista
linhas_invertidas = linhas[::-1]

# Gravar as linhas invertidas no arquivo "invertido.txt"
with open("invertido.txt", "w") as arquivo_invertido:
    arquivo_invertido.writelines(linhas_invertidas)

