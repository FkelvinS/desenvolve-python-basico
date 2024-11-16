#Importando bibliotecas
import random, math 

#Solicitando ao usuário a quantidade de valores que deseja fazer o cálculo
n = int(input("Digite a quantidade de valores: "))
soma = 0

#Processamento
for i in range(n):
    valor = random.randint(0, 100)
    print(valor)
    soma += valor

#Saída de dados
print("A soma dos valores é:", soma)
print(f"A raíz quadrada da soma é: {math.sqrt(soma): .2f}")