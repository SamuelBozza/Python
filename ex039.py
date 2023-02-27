'''
FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
-SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR.
-SE É A HORA DE SE ALISTAR.
-SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTO OU QUE PASSOU DO PRAZO.
'''
#PARAMETRO USADO PARA ALISTAMENTO = 18 ANOS
#IMPORTAÇÃO
from datetime import date
#DADOS DA DATA ATUAL *ANO*
data_atual = date.today()
ano_atual:int = data_atual.year
#ENTRA DE DADOS DO NASCIMENTO DO USUÁRIO:
nascimento = int(input('Em que ano você nasceu?:'))
#CALCULOS PARA CHEGAR NA IDADE DO USUÁRIO:
idade = ano_atual - nascimento
if idade < 18:
    print('Você deve se alistar em {} anos!'.format(18-idade))
elif idade == 18:
    print('É a hora de se alistar, jovem!')
else:
    print('Você deveria ter se alistado {} anos atrás!'.format(idade-18))
