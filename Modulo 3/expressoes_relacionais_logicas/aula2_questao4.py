#entrada de dados
#classes disponiveis : guerreiro, mago ou arqueiro
#pontos atribuidos de força e magia

classe = input('Escolha a sua classe(guerreiro, mago ou arqueiro): ')
forca = int(input('Digite os pontos de força (de 1 a 20): '))
magia = int(input('Digite os pontos de magia (de 1 a 20): '))

#processamento
#caso a classe seja guerreiro devera ter forca >=15 e magia <=10
#mago devera ter forca <=10 e magia >=15
#arqueiro devera ter forca e magia >5 e <15

guerreiro = classe =="guerreiro" and forca >=15 and forca <=20 and magia <=10
mago = classe =="mago" and forca <=10 and magia >=15 and magia <=20
arqueiro = classe =="arqueiro" and forca >=5 and forca <=15 and magia >=5 and magia <=15
aprovado = guerreiro or mago or arqueiro

#saída de dados

print(f"Pontos de atributo consistentes com a classe escolhida: {aprovado}")

