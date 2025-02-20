# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Exibe o nome em forma de escada usando compreensão de listas
for i in range(1, len(nome) + 1):
    print(nome[:i])
