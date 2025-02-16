# Lista de horas trabalhadas
horas_trabalhadas = [40, 37, 45, 40, 40, 48]

# Definição dos valores por hora
ganho_por_hora = 20
hora_extra = 25

# Criando a lista pagamentos com compreensão de listas
pagamentos = [
    ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40)
    for hora in horas_trabalhadas
]

# Exibindo a lista de pagamentos
print(pagamentos)
