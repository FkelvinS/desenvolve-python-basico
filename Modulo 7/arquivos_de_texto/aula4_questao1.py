import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Obtém o diretório atual onde o script está sendo executado
diretorio_atual = os.path.abspath(os.getcwd())

# Caminho completo do arquivo
caminho_completo = os.path.join(diretorio_atual, nome_arquivo)

# Escreve a frase no arquivo
with open(caminho_completo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Imprime o caminho completo do arquivo salvo
print(f"Frase salva em {caminho_completo}")
