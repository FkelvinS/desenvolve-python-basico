import string

def limpar_texto(frase):
    # Remove espaços e pontuação, e converte para minúsculas
    return "".join(letra.lower() for letra in frase if letra.isalnum())

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == "fim":
        break  # Encerra o programa

    frase_limpa = limpar_texto(frase)
    if frase_limpa == frase_limpa[::-1]:  # Compara a string com ela invertida
        print(f'"{frase}" é palíndromo\n')
    else:
        print(f'"{frase}" não é palíndromo\n')
