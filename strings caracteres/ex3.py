# Neste exercício, você criará um programa em Python que identifica a(s)
# palavras(s) mais longa(s) em um arquivo.
# • Seu programa deve exibir uma mensagem que inclua o tamanho da
# palavra mais longa, juntamente com todas as palavras desse
# comprimento que ocorreram no arquivo. Desconsidere sinais de
# pontuação.

import re

# Ler o arquivo e armazenar o conteúdo em uma string
with open("nome_do_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()

# Remover sinais de pontuação e manter apenas as palavras
conteudo = re.sub(r'[^\w\s]', '', conteudo)

# Separar a string em palavras individuais
palavras = conteudo.split()

# Encontrar o tamanho da palavra mais longa
tamanho_max = max(len(palavra) for palavra in palavras)

# Identificar todas as palavras com o tamanho máximo
palavras_max = [palavra for palavra in palavras if len(palavra) == tamanho_max]

# Exibir a mensagem com o tamanho da palavra mais longa e as palavras correspondentes
print(
    f"A palavra mais longa tem {tamanho_max} caracteres: {', '.join(palavras_max)}")
