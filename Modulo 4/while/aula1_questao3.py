#Entrada de dados
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

m = (n1 + n2 + n3) /3
print(m)
#Processamento e saída 
if m >=60 :
    print('Aprovado')

elif m >= 40 :
    print('Recuperação')

else :
    print('Reprovado')

print('Fim')