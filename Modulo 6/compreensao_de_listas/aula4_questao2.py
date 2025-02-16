# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Definição das vogais
vogais = "aeiouAEIOU"

# Lista de vogais ordenada alfabeticamente
lista_vogais = sorted([letra for letra in frase if letra in vogais])

# Lista de consoantes (removendo espaços)
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]

# Exibe os resultados
print("Vogais:", lista_vogais)
print("Consoantes:", lista_consoantes)
