import random
from collections import Counter

# Gerar duas listas com 20 valores inteiros aleatórios entre 0 e 50
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Criar a lista de interseção sem duplicatas
intersecao = sorted(set(lista1) & set(lista2))

# Contar a frequência de cada elemento em ambas as listas
contador_lista1 = Counter(lista1)
contador_lista2 = Counter(lista2)

# Imprimir as listas e os resultados
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista de interseção (ordenada):", intersecao)

# Frequência de elementos na interseção, apenas se o elemento aparecer nas duas listas
print("\nFrequência de elementos na interseção:")

for elemento in intersecao:
    print(f"{elemento}:")
    print(f"  Lista 1: {contador_lista1[elemento]} vez(es)")
    print(f"  Lista 2: {contador_lista2[elemento]} vez(es)")

