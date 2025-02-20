# Solicita o número ao usuário
numero = input("Digite o número: ")

# Verifica se tem 8 dígitos e adiciona o '9' na frente
if len(numero) == 8:
    numero = "9" + numero

# Formata o número com o separador "-"
numero_formatado = numero[:5] + "-" + numero[5:]

# Exibe o número formatado
print("Número completo:", numero_formatado)
