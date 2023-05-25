# Exercício 4
# • Escreva um programa que exiba a(s) palavra(s) que ocorrera(m) com
# mais frequência em um arquivo e quantas vezes a(s) palavra(s)
# aparece(m).
# • Seu programa deve começar lendo o nome do arquivo do usuário.
# • Em seguida, ele deve encontrar a(s) palavra(s) mais frequente(s),
# ignorando letras maiúsculas ou minúsculas e a pontuação.
# – Desta forma, por exemplo, as palavras apple, apple!, Apple, APPLE
# e ApPlE devem todas ser contadas como uma única palavra.


import re
from collections import Counter

# Ler o nome do arquivo do usuário
nome_arquivo = input("Digite o nome do arquivo: ")

# Ler o conteúdo do arquivo e armazenar em uma string
with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

# Remover a pontuação e converter para minúsculas
conteudo = re.sub(r'[^\w\s]', '', conteudo).lower()

# Separar a string em palavras individuais
palavras = conteudo.split()

# Contar a frequência de cada palavra
contador = Counter(palavras)

# Encontrar a contagem máxima de frequência
max_frequencia = max(contador.values())

# Identificar todas as palavras com a contagem máxima de frequência
palavras_max_frequencia = [
    palavra for palavra, frequencia in contador.items() if frequencia == max_frequencia]

# Exibir as palavras mais frequentes e suas contagens
print("Palavras mais frequentes:")
for palavra in palavras_max_frequencia:
    print(f"{palavra}: {contador[palavra]} ocorrências")
