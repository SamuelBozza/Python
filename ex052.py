'''
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO.
'''
#ENTRADA DE DADOS.
núm = int(input('Digite um número:'))
tot = 0
#ESTRUTURA FOR
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\033[m\nO número {} foi divisível {} vezes'.format(núm, tot)) #PRINT
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')