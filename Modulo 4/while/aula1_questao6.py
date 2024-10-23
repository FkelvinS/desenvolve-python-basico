#Entrada de dados e inicialização de valores
n = int(input('Qual a quantidade de experimentos? '))
cont = 0
sapos, ratos, coelhos = 0, 0, 0

#Processamento
while cont <n :
    quantia = int(input('Quantos? '))
    tipo = input('Qual tipo? ')
    cont += 1 
    if tipo == "S" :
        sapos += quantia
    elif tipo == "R" :
        ratos += quantia
    elif tipo == "C" :
        coelhos += quantia
    else:
        print("Inválido!!")

total = sapos + ratos + coelhos
porcentagem_S = (sapos / total) *100  
porcentagem_R = (ratos / total) *100
porcentagem_C = (coelhos / total) *100

#Saída
print("Total de cobaias:", sapos + ratos + coelhos)
print("Total de Sapos:", sapos)
print("Total de Ratos:", ratos)
print("Total de Coelhos:", coelhos)
print(f'Percentual de sapos: {porcentagem_S: .2f}%')
print(f'Percentual de ratos: {porcentagem_R: .2f}%')
print(f'Percentual de coelhos: {porcentagem_C: .2f}%')
