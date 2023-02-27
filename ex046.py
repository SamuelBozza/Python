'''
FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE
ARTIFÍCIO, INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELAS.
'''
#IMPORTAÇÕES
from time import sleep
#FOR.
for contagem in range(10,0, -1):
    print(f'Contagem regressiva: {contagem}')
    sleep(0.5)
print('Os fogos de artifício foram liberados!')