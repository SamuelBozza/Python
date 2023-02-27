'''
Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
#DEFININDO
soma = 0
cont = 0
#ESTRUTURA FOR
for números in range(1, 501, 2):
    if números % 3 == 0:
        cont += 1
        soma += números
#PRINT
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))