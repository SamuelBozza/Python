'''
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50.
'''
#FOR.
for número in range(1, 51):
    if (número%2) == 0:
        print(número, end=' ')