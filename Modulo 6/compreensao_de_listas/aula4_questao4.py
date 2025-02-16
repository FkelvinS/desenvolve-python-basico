# Listas de alunos e notas
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Criando a lista de aprovados com compreensão de listas
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

# Exibindo a lista de aprovados
print(aprovados)
