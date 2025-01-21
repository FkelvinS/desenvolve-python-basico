import random

# Gerar aleatoriamente o número de elementos entre 5 e 20
num_elementos = random.randint(5, 20)

# Gerar uma lista com valores aleatórios entre 1 e 10 com tamanho igual a num_elementos
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcular a soma e a média dos valores da lista
soma = sum(elementos)
media = soma / num_elementos

# Imprimir os resultados
print("Lista de elementos:", elementos)
print("Soma dos valores da lista:", soma)
print("Média dos valores da lista:", media)
