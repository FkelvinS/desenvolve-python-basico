#Importando bibliotecas
import emoji

#Apresentando ao usuário emojis disponíveis
print("Emojis disponíveis: ")
print(emoji.emojize(':red_heart:'), " - :red_heart:")
print(emoji.emojize(':thumbs_up:'), " - :thumbs_up:")
print(emoji.emojize(':enraged_face:'), " - :enraged_face:")
print(emoji.emojize(':partying_face:'), " - :partying_face:")
print("Digite uma frase e ela será emojizada")
print(f"Olá mundo! :red_heart:")
print("Frase emojizada:")
print("Olá mundo!", emoji.emojize(':red_heart:'))

#Solicitando ao usuário uma frase que deseja emojizar
frase = input("Digite a frase que deseja emojizar e o emoji na próxima linha: ")
emoji = input("Digite o código do emoji: ")

#Imprimindo frase emojizada: