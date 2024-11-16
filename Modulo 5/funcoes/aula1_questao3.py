#Importando bibliotecas
import random

#Gerando valor aleatório entre 1 e 10
valor = random.randint(1, 10)
print(valor)
#Usuário tenta adivinhar
while True: 
    resposta = int(input("Adivinhe o número entre 1 e 10: "))

    if resposta == valor: 
        print(f"Correto! O número é {valor}")
        break

    elif resposta <valor:
        print("Muito baixo, tente novamente!")

    else:
        print("Muito alto, tente novamente!")
    