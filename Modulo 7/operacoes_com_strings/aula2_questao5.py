import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) > 3:
            meio = list(palavra[1:-1])  # Pegamos as letras internas
            random.shuffle(meio)  # Embaralhamos as letras internas
            return palavra[0] + "".join(meio) + palavra[-1]  # Reconstruímos a palavra
        return palavra  # Palavras curtas não são alteradas

    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in frase.split()]
    return " ".join(palavras_embaralhadas)

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")
resultado = embaralhar_palavras(frase)

print("Frase embaralhada:", resultado)
