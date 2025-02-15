import random

# Passo 1: Gerar uma lista com 20 números aleatórios entre -10 e 10
numeros = [random.randint(-10, 10) for _ in range(20)]
print("Original:", numeros)

# Passo 2: Encontrar o intervalo com mais números negativos consecutivos
maior_inicio = 0   # Índice onde a maior sequência começa
maior_fim = 0      # Índice onde a maior sequência termina
contador = 0       # Contagem de números negativos na sequência atual
inicio_temp = 0    # Índice do início da sequência temporária

# Percorre a lista para encontrar a maior sequência de negativos
for i in range(len(numeros)):
    if numeros[i] < 0:  # Se o número for negativo
        if contador == 0:  # Se for o começo de uma nova sequência
            inicio_temp = i
        contador += 1
    else:
        if contador > (maior_fim - maior_inicio):  # Verifica se foi a maior sequência encontrada
            maior_inicio = inicio_temp
            maior_fim = i  # Fim é o primeiro número positivo encontrado
        contador = 0  # Reinicia o contador

# Se a última sequência foi a maior, atualiza os índices
if contador > (maior_fim - maior_inicio):
    maior_inicio = inicio_temp
    maior_fim = len(numeros)  # O fim será o final da lista

# Passo 3: Remover a sequência da lista
del numeros[maior_inicio:maior_fim]

# Passo 4: Exibir a lista após a remoção
print("Editada:", numeros)
