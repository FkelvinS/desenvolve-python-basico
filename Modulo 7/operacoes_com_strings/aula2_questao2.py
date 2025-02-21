# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Lista de vogais
vogais = "aeiouAEIOU"

# Substitui as vogais por "*"
frase_modificada = "".join("*" if letra in vogais else letra for letra in frase)

# Exibe a frase modificada
print("Frase modificada:", frase_modificada)
