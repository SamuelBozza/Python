from calendar import isleap
#entrada de dados
ano = int(input('Entre com um ano: '))

if isleap(ano):
    print('É bissexto')
else:
    print('Não é bissexto')