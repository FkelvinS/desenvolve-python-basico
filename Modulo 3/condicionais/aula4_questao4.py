#entrada de dados
#solicitar ao usuario a distancia da entrega
#em quilometros e o peso do pacote
distancia, peso = float(input('Digite a distância em Km: ')), float(input('Digite o peso do produto: '))

#processamento

if distancia <= 100:
    custo_por_kg = 1.0

if 101 <= distancia <= 300:
    custo_por_kg = 1.5

if distancia > 300:
    custo_por_kg = 2.0

frete = custo_por_kg * peso

if peso > 10:
    frete = frete + 10

#saída de dados
print(f'O valor do frete é R${frete:.2f} ')