# Lista de URLs
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

# Extraindo os domínios com fatiamento
dominios = [url[4:-4] for url in urls]

# Exibindo o resultado
print(dominios)
