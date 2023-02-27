'''
REFAÇA O DESAFIO 9, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR.
'''
#ENTRADA DE DADOS
n = int(input('Entre com um valor para a tábuada: '))
#FOR.
for numeros in range(1,11):
    print('{} x {} = {}'.format(numeros, n, numeros*n))