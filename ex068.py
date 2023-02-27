'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint #IMPORTAÇÕES
print('-='*13)
print('VAMOS JOGAR PAR OU ÍMPAR') #TITTLE
print('-='*13)
soma = soma1 = cont = 0 #DEFINIÇÕES PARA 0
computador = randint(1, 11) #NÚMERO GERADO ALEATORIAMENTE
resultado = ' ' #RESULTADOS POSSIVEIS
while True:
    valor = int(input('Diga um valor: ')) #ENTRADA DO VALOR
    escolha = ' ' #ESCOLHA DO PARTICIPANTE
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).upper()[0].strip() #ENTRADA DE PAR OU IMPAR
    soma1 = valor + computador #SOMANDO O TOTAL ENTRE O VALOR E O COMPUTADOR
    soma = (valor+computador)%2 #SOMANDO PARA SABER SE O RESULTADO É IMPAR OU PAR
    if soma == 0: # PAR
        resultado = 'Par'
    else: # ÍMPAR
        resultado = 'Impar'
    print('-'*50)
    print(f'Você Jogou {valor} e o computador {computador}. Total de {soma1} deu {resultado[:10]}')
    print('-'*50)
    if escolha == resultado[0]: # JOGADOR VENCE
        print('Você VENCEU!')
        cont +=1 # CONTADOR DE PARTIDAS VENCIDAS
    else: # MAQUINA VENCE
        print('Você PERDEU!')
        break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {cont} vezes.')