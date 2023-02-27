l = float(input('Entre com quantos Metros de largura tem a parede:'))
a = float(input('Entre com quantos Metros de Altura tem a parede:'))
r = l * a
t = r / 2
print('Sua parede tem: {:.2f}Metros quadrados \nE você precisara de {:.2f}Litros para pintar toda a parede!'.format(r, t))
