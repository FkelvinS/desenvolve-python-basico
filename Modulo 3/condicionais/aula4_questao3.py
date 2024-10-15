#entrada de dados
#solicitar ao usuario um ano
ano = int(input('Insira um ano: '))

#processamento
#verifica se o ano é bissexto
if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 00):
    print('Bissexto')
else:
    print('Não bissexto')