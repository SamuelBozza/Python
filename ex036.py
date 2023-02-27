casa = float(input('Qual o valor da casa?:'))
salário = float(input('Qual seu salário atual?:'))
anos = int(input('Em quantos anos deseja pagar a casa?:'))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(casa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
