# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Define as vogais
vogais = "aeiouAEIOU"

# Lista para armazenar os índices das vogais
indices_vogais = [i for i in range(len(frase)) if frase[i] in vogais]

# Exibe os resultados
print(len(indices_vogais), "vogais")
print("Índices", indices_vogais)
