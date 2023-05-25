# Faça um programa que:
# • Peça um string para o usuário
# • Imprima uma nova string substituindo as vogais minúsculas por vogais
# maiúsculas.

def substituir_vogais(string):
    vogais_min = 'aeiou'
    vogais_mai = 'AEIOU'

    for i in range(len(vogais_min)):
        string = string.replace(vogais_min[i], vogais_mai[i])

    return string


# Solicita uma string ao usuário
entrada = input("Digite uma string: ")

# Chama a função para substituir as vogais
resultado = substituir_vogais(entrada)

# Imprime a nova string com as vogais substituídas
print("Nova string: " + resultado)
