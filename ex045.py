'''
CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.
'''
#IMPORTAÇÕES
from random import randint
from time import sleep
#DEFININDO OS ITENS
itens = ('Pedra','Papel','Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
#PRINTS
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÓ!!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
#CONVERTENDO PARA IF/ELIF
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('\033[7;37;40mEMPATE\033[m')
    elif jogador == 1:
        print('\033[7;32;40mJOGADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[7;31;40mCOMPUTADOR VENCE\033[m')
    else:
        print('\033[7;31;40mJOGADA INVÁLIDA!\033[m')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('\033[7;31;40mCOMPUTADOR \033[m')
    elif jogador == 1:
        print('\033[7;37;40mEMPATE\033[m')
    elif jogador == 2:
        print('\033[7;32;40mJOGADOR VENCE\033[m')
    else:
        print('\033[7;31;40mJOGADA INVÁLIDA!\033[m')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print('\033[7;32;40mJOGADOR VENCE\033[m')
    elif jogador == 1:
        print('\033[7;31;40mCOMPUTADOR VENCE\033[m')
    elif jogador == 2:
        print('\033[7;37;40mEMPATE\033[m')
    else:
        print('\033[7;31;40mJOGADA INVÁLIDA!\033[m')