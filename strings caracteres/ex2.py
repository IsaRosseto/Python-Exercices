# Peça ao usuário uma string:
# • Imprima se essa string é um palíndromo ou não.
# • Palíndromo é uma palavra ou frase(normalmente, ignorando-se os
# espaços em branco) que se pode ler, indiferentemente, da esquerda
# para a direita ou vice-versa.
# • Exemplos: “ovo”, “a grama é amarga”

def eh_palindromo(string):
    # Remover espaços em branco da string e converter para letras minúsculas
    string = string.replace(" ", "").lower()

    # Verificar se a string é igual à sua versão invertida
    if string == string[::-1]:
        return True
    else:
        return False


# Solicita uma string ao usuário
entrada = input("Digite uma string: ")

# Verifica se a string é um palíndromo
if eh_palindromo(entrada):
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")
