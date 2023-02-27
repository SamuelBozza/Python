'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
#ENTRADA DE DADOS
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
escolha = 0
#ESTRUTURA WHILE
while escolha != 5:
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa')
    escolha = int(input('>>>>> Qual é sua opção?'))
    if escolha == 1: #SOMA
        print('A soma de {} e {} é: {}'.format(n1,n2,n1+n2))
    if escolha == 2: #MULTIPLICAÇÃO
        print('A multiplicação de {} e {} é: {}'.format(n1,n2,n1*n2))
    if escolha == 3: #MAIOR NÚMERO
        if n1 > n2:
            print('Entre os números {} e {}, o maior é: {}'.format(n1,n2,n1))
        elif n2 > n1:
            print('Entre os números {} e {}, o maior é: {}'.format(n1,n2,n2))
    if escolha == 4: #REESCREVER NÚMEROS
        n1 = int(input('Entre com um novo primeiro número: '))
        n2 = int(input('Entre com um novo segundo número: '))
    if escolha > 5: #SE NÃO FOR NENHUM NÚMERO ENTRE 1 E 5 DAR COMANDO INVÁLIDO
        print('Número inválido, tente novamente:')
print('Fim do programa, volte sempre!')

