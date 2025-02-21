# Lista com os meses do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Solicita a data de nascimento ao usuário
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa o dia, mês e ano
dia, mes, ano = data.split("/")

# Converte o mês para o nome correspondente (subtrai 1 pois listas começam no índice 0)
mes_extenso = meses[int(mes) - 1]

# Exibe a data formatada
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")
