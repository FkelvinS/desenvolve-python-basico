import os
import re

# Define os nomes dos arquivos
nome_arquivo_origem = "frase.txt"
nome_arquivo_destino = "palavras.txt"

# Obtém o diretório atual onde o script está sendo executado
diretorio_atual = os.path.abspath(os.getcwd())

# Caminhos completos dos arquivos
caminho_origem = os.path.join(diretorio_atual, nome_arquivo_origem)
caminho_destino = os.path.join(diretorio_atual, nome_arquivo_destino)

# Lê o conteúdo do arquivo original
try:
    with open(caminho_origem, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print(f"Arquivo {nome_arquivo_origem} não encontrado.")
    exit()

# Remove caracteres não alfabéticos e separa palavras
palavras = re.findall(r"\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b", conteudo)

# Escreve as palavras no novo arquivo, uma por linha
with open(caminho_destino, "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(palavras))

# Lê e imprime o conteúdo do novo arquivo
with open(caminho_destino, "r", encoding="utf-8") as arquivo:
    print(arquivo.read())
