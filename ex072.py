'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
#CRIANDO TUPLA COM ELEMENTOS SENDO OS NÚMEROS POR ESCRITO
núm = 'zero','um','dois','tres','quatro','cinco','seis','sete',\
      'oito','nove','dez','onze','doze','treze','catorze',\
      'quinze','dezesseis','dezesete','dezoito','dezenovo','vinte'
while True:
    entrada = int(input('Entre com um número de 1 a 20: ')) #ENTRADA DO NÚMERO DESEJADO
    if 0 <= entrada <= 20:
        print(f'Você digitou o número {núm[entrada]}')
        opção = str(input('Deseja continuar? [S/N]' )).strip().upper()[0]
        if opção not in 'Ss':
            break