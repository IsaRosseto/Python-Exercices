# Gerar e gravar números pares e ímpares em arquivos separados:
# • Números de 0 a 999.
# • Números pares no arquivo pares.txt
# • números ímpares no arquivo impares.txt

def eh_par(numero):
    return numero % 2 == 0


# Gerar números pares e ímpares e gravar nos arquivos
with open("pares.txt", "w") as arquivo_pares, open("impares.txt", "w") as arquivo_impares:
    for numero in range(1000):
        if eh_par(numero):
            arquivo_pares.write(str(numero) + "\n")
        else:
            arquivo_impares.write(str(numero) + "\n")
