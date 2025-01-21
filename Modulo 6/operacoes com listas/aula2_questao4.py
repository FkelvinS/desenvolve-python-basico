def combinar_listas(lista1, lista2):
    lista_combinada = []
    # Encontra o comprimento mínimo entre as duas listas
    min_len = min(len(lista1), len(lista2))
    
    # Intercala os elementos das duas listas até o tamanho mínimo
    for i in range(min_len):
        lista_combinada.append(lista1[i])
        lista_combinada.append(lista2[i])

    # Adiciona os elementos restantes da maior lista, se houver
    lista_combinada.extend(lista1[min_len:])
    lista_combinada.extend(lista2[min_len:])
    
    return lista_combinada

# Recebe duas listas de números do usuário
lista1 = list(map(int, input("Digite os números da primeira lista separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os números da segunda lista separados por espaço: ").split()))

# Chama a função para combinar as listas
lista_combinada = combinar_listas(lista1, lista2)

print("Lista combinada:", lista_combinada)
