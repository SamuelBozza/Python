#entrada de dados
km = int(input('Entre com quantos km o carro consta:'))
#resultado se a entrada de dados foi maior q 80 o usuário sera multado.
if km > 80:
    print('Parabéns, você foi multado! e tera que pagar uma multa de ${}'.format((km-80)*7))
else:
    print('Parabéns, você está na lei!')