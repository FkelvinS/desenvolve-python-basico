#Entrada de dados e inicialização de valores
n = int(input('Qual a quantidade de respondentes? '))

cont = 0
soma = 0
qtd = 1
while cont <n :
    idade = int(input(f'Qual a idade do respondente {qtd}? '))
    soma += idade
    cont += 1
    qtd += 1
media = soma / n
print(f'A média das idades é {media}')