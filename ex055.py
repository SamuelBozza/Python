'''
FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
'''
#ESTRUTURA FOR
for p in range(1,6):
    peso = float(input('Quanto a {} pessoa pesa?: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior: #SE 'MAIOR' FOR MAIOR QUE 'PESO' O 'MAIOR' PASSA A SER O PESO.
            maior = peso
        if peso < menor: #SE 'MENOR' FOR MENOR QUE 'PESO' O 'MENOR' PASSA A SER O PESO.
            menor = peso
#PRINT
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
