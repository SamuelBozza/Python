import math
num1 = float(input('Entre com o valor do cateto oposto:'))
num2 = float(input('Entre com o valor do cateto adjacente:'))
h = math.hypot(num1, num2)
print('A hipotenusa é: {:.2f}!'.format(h))