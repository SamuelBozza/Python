#entrada de dados
n = int(input('Quantos km você ira rodar?:'))

if n <= 200:
    print('Você tera que pagar uma passagem de ${}, tenha uma boa viagem!'.format(n*0.50))
else:
    print('Você tera que pagar uma passagem de ${}, tenha uma boa viagem!'.format(n*0.45))