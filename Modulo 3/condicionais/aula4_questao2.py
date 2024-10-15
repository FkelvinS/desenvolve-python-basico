#entrada de dados 
#solicitar ao usuario a avaliacao de um filme, entre 1 e 5

nota = int(input('Digite sua avaliação do filme(1 a 5): '))

#processamento e saída
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

if nota == 1:
    print('Excelente!')

if nota == 2:
    print('Muito bom!')

if nota == 3:
    print('Bom!')

if nota == 4:
    print('Regular.')

if nota == 5:
    print('Ruim.')