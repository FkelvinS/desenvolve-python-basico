#Entrada de dados
comprimento=int(input('Qual o comprimento do terreno?'))
largura=int(input('Qual a largura do terreno?'))
preco_m2=float(input('Qual o preço do m2?'))
#Fórmulas:
area_m2 = comprimento*largura
preco_total = preco_m2*area_m2

#Saída de dados
print(f"Seu terreno tem {area_m2}m2 e custa R${preco_total:,.2f}")