'''
ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO
NA TELA UMA MENSAGEM: -O PRIMEIRO VALOR É MAIOR;-O SEGUNDO É MAIOR;-NÃO EXISTE VALOR MAIOR, OS 2 SÃO IGUAIS.
'''
#ENTRADA DOS VALORES.
n1 = int(input('Entre com o primeiro valor:'))
n2 = int(input('Entre com o segundo valor:'))
#CALCULOS PARA SABER QUAL É MAIOR.
if n1 > n2:
    print('O primeiro valor é MAIOR')
elif n1 < n2:
    print('O Segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são\033[7;31;40mIGUAIS!\033[m')