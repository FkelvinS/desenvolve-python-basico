# Entrada de dados

# Produto 1
print('PRODUTO 1:')
produto1=input('Digite o nome do produto 1: ')
preco_un_p1=float(input('Digite o preço unitário do produto 1: '))
qntd_p1=int(input('Digite a quantidade do produto 1: '))

# Produto 2
print('PRODUTO 2:')
produto2=input('Digite o nome do produto 2: ')
preco_un_p2=float(input('Digite o preço unitário do produto 2: '))
qntd_p2=int(input('Digite a quantidade do produto 2: '))


# Produto 3
print('PRODUTO 3:')
produto3=input('Digite o nome do produto 3: ')
preco_un_p3=float(input('Digite o preço unitário do produto 3: '))
qntd_p3=int(input('Digite a quantidade do produto 3: '))

#Processamento
valorp1 = preco_un_p1*qntd_p1
valorp2 = preco_un_p2*qntd_p2
valorp3 = preco_un_p3*qntd_p3
valor_total=valorp1+valorp2+valorp3

#Saída de dados
print(f'Valor total dos seus produtos: R${valor_total:,.2f}')