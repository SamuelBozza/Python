d = int(input('Quantos dias alugado?:'))
km = int(input('Quantos Km rodados?:'))
r =  (d * 60) + (km * 0.15)
print('O total a pagar é de {}!'.format(r))