import csv

livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 384],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 552],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", 2011, 412],
    ["O Alquimista", "Paulo Coelho", 1988, 208]
]

# Abrir o arquivo para escrita
with open('meus_livros.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    # Criar o objeto writer
    escritor = csv.writer(arquivo)
    
    # Escrever o cabeçalho
    escritor.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escrever os dados dos livros
    for livro in livros:
        escritor.writerow(livro)


