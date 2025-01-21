import random

# Gerar uma lista de 20 valores inteiros aleatórios entre -100 e 100
lista_original = [random.randint(-100, 100) for _ in range(20)]

# Criar uma nova lista ordenada sem modificar a original
lista_ordenada = sorted(lista_original)

# Obter os índices do maior e menor valor
indice_maior = lista_original.index(max(lista_original))
indice_menor = lista_original.index(min(lista_original))

# Imprimir os resultados
print("Lista ordenada (sem modificar a original):", lista_ordenada)
print("Lista original:", lista_original)
print("Índice do maior valor da lista:", indice_maior)
print("Índice do menor valor da lista:", indice_menor)
