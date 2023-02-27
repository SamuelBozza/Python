#entrada de dados
n1 = int(input('Entre com o primeiro número:'))
n2 = int(input('Entre com o segundo número:'))
n3 = int(input('Entre com o terceiro número:'))

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:
    m = n1
if n2 > n1 and n2 > n3:
    m = n2
if n3 > n1 and n3 > n2:
    m = n3
print('O menor numéro é {}'.format(menor))
print('O maior número é {}'.format(m))
