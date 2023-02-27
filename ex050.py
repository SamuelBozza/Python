'''
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERO-O
'''
#ENTRADA DE DADOS.
soma = 0
for numeros in range(1,7):
    número = int(input('Entre com um número inteiro: '))
    if (número%2) == 0:
        soma+= número
print(soma)
