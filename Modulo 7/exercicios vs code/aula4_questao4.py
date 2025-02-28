import random

def carregar_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
        palavras = [linha.strip() for linha in f.readlines()]
    return palavras

def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        estagios = f.read().split("\n\n")
    return estagios

def imprime_enforcado(erros, estagios):
    print(estagios[erros])

def jogar():
    palavras = carregar_palavras()
    estagios = carregar_enforcado()
    palavra = random.choice(palavras).upper()
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = set()
    tentativas = 0
    
    print("Bem-vindo ao Jogo da Forca!")
    print(" ".join(letras_descobertas))
    
    while tentativas < 6 and "_" in letras_descobertas:
        letra = input("Digite uma letra: ").strip().upper()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Digite apenas uma letra válida!")
            continue
        
        if letra in letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_descobertas[i] = letra
        else:
            tentativas += 1
            letras_erradas.add(letra)
            print("Letra errada!")
        
        imprime_enforcado(tentativas, estagios)
        print(" ".join(letras_descobertas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
    
    if "_" not in letras_descobertas:
        print("Parabéns! Você venceu!")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()
