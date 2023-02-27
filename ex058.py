'''
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até
acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
#IMPORTAÇÕES
import random
from time import sleep
#DEFININDO UM NÚMERO ALEÁTORIO
quantidade = random.randint(1,11)
tentativa = 1 #definindo as tentativas pra 0
#PRINTS
print('Sou um computador...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
#ENTRADA DE DADOS
n = int(input('Qual seu palpite? '))
#ESTRUTURA WHILE
while n != quantidade:
    n = int(input('Errou! tente novamente: '))
    tentativa = tentativa + 1
    if n == quantidade:
        print('Você acertou! o número escolhido foi {} e você acertou com {} tentativas, parabéns!'.format(quantidade, tentativa))


