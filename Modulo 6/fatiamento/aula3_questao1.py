# Solicita ao usuário que informe uma quantidade indefinida de números inteiros (com pelo menos 4 valores)
numeros = []

print("Digite os números inteiros (digite '0' para finalizar, mas tenha pelo menos 4 valores):")
while len(numeros) < 4:
    numero = int(input())
    if numero == 0 and len(numeros) >= 4:
        break
    elif numero != 0:
        numeros.append(numero)

# Imprime a lista original
print(f"\nLista original: {numeros}")

# Imprime os 3 primeiros elementos
print(f"Os 3 primeiros elementos: {numeros[:3]}")

# Imprime os 2 últimos elementos
print(f"Os 2 últimos elementos: {numeros[-2:]}")

# Imprime a lista invertida
print(f"Lista invertida: {numeros[::-1]}")

# Imprime os elementos de índice par
print(f"Elementos de índice par: {numeros[::2]}")

# Imprime os elementos de índice ímpar
print(f"Elementos de índice ímpar: {numeros[1::2]}")
