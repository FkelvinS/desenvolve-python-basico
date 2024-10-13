#entrada de dados
#idade
#quantidade de jogos jogados
#quantidade de vezes que venceu

idade = int(input('Qual a sua idade? '))
jogados = input('Já jogou pelo menos 3 jogos de tabuleiro? ')
vencidos = int(input('E quantos você já venceu? '))

#processamento
#ter entre 16 e 18 anos
#já ter jogado pelo menos 3 jogos
#já ter vencido pelo menos 1 jogo

idade_aprovada = idade >= 16 and idade <=18
jogados_aprovados = jogados =="Sim" or jogados =="sim"
vencidos_aprovados = vencidos >=1
podera_participar = idade_aprovada and jogados_aprovados and vencidos_aprovados
#saída
#caso todos sejam true, poderá participar

print(f"Apto para ingressar no clube de jogos de tabuleiro: {podera_participar}")