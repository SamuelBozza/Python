'''
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM
A MAIORIDADE E QUANTAS JÁ SÃO MAIORES.
CONSIDERANDO MAIORIDADE = 21 ANOS
'''
#IMPORTAÇÃO
from datetime import date
atual = date.today().year #DEFININDO O ANO ATUAL
totmaior = 0
totmenor = 0
#ESTRUTURA FOR
for pess in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu?: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
#PRINT
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))