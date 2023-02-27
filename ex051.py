'''
DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.
'''
#ENTRADA DE DADOS
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
#ESTRUTURA FOR
for c in range(primeiro, décimo + razão, razão):
    print('{}'.format(c), end='->')
print('ACABOU')