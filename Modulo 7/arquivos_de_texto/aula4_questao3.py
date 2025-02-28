import os

# Nome do arquivo contendo o roteiro
nome_arquivo = "estomago.txt"

# Obtém o diretório atual onde o script está sendo executado
diretorio_atual = os.path.abspath(os.getcwd())

# Caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo)

# Lê o conteúdo do arquivo
try:
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
except FileNotFoundError:
    print(f"Arquivo {nome_arquivo} não encontrado.")
    exit()

# 1. Exibir as primeiras 25 linhas
total_linhas = len(linhas)
print("Primeiras 25 linhas do arquivo:")
print("".join(linhas[:25]))

# 2. Exibir o número total de linhas do arquivo
print(f"\nNúmero total de linhas: {total_linhas}")

# 3. Encontrar a linha com maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres:\n{linha_mais_longa.strip()}")

# 4. Contar menções aos nomes "Nonato" e "Íria" (ignorando maiúsculas/minúsculas)
nonato_count = sum(1 for linha in linhas if "nonato" in linha.lower())
iria_count = sum(1 for linha in linhas if "íria" in linha.lower().split())

print(f"\nMenções ao nome 'Nonato': {nonato_count}")
print(f"Menções ao nome 'Íria': {iria_count}")
