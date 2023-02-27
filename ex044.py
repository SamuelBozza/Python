'''
ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇAO DE PAGAMENTO:
-À VISTA DINHEIRO/CHEQUE:10% DE DESCONTO
-À VISTA NO CARTÃO: 5% DE DESCONTO
-EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
-3X OU MAIS NO CARTÃO: 20% DE JUROS
'''
print('{:=^40}'.format(' LOJAS SAMUEL '))
#ENTRADA DE DADOS
preço = float(input('Entre com o valor do produto:'))
condição = int(input('Por favor, Selecione uma forma de pagamento:\n[ 1 ] À vista(10% Desconto);\n[ 2 ] À vista no cartão(5% desconto);\n[ 3 ] Em até 2X no cartão(preço normal);\n[ 4 ] 3X ou Mais no cartão(20% desconto).\nQual a forma de pagamento?:'))
#CONVERTANDO PARA IF/ELIF
if condição == 1:
    x = preço*0.10
    x1 = preço-x
    print('Com 10% de desconto o preço final sera:{}'.format(x1))
elif condição == 2:
    x = preço *0.05
    x1 = preço-x
    print('Com 5% de desconto o preço final sera:{}'.format(x1))
elif condição == 3:
    x = preço/2
    print('Pagando em 2x no cartão, Você tera que pagar 2 parcelas de {} cada!'.format(x))
elif condição == 4:
    parcelas = int(input('Em quantas vezes deseja pagar?:'))
    total = preço + (preço *0.20)
    parcela = total / parcelas
    print('Com 20% de desconto e pagando em {}X, Você tera que pagar parcelas de {:.2f} COM JUROS!'.format(parcelas, total))
else:
    total = 0
    print('\033[7;30;41mOPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!\033[m')
