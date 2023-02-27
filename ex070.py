'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
print('-'*30)
print('      LOJA SUPER BARATÃO      ')
print('-'*30)
tot = milreais = menor = cont = 0 #DEFINDO PARA 0
barato = ' ' #NOME DO PRODUTO MAIS BARATO
while True:
    continuar = ' '
    produto = str(input('Nome do produto: ')) #ENTRADA DO NOME DO PRODUTO
    preço = float(input('Preço: R$')) #ENTRADA DO PREÇO
    cont += 1 #CONTANDO OS PREÇOS PARA PEGAR O MENOR
    tot += preço #SOMANDO O TOTAL
    if preço > 1000: #VENDO QUANTOS PRODUTOS CUSTARAM MAIS DE R$1000
        milreais += 1
    if cont == 1 or preço < menor: #DEFININDO O MENOR PREÇO E O NOME DO PRODUTO
        menor = preço
        barato = produto
    while continuar not in 'SN': #ESTRUTURA DE CONTINUAÇÃO
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N': #ESTRUTURA PARA PARAR
        break #*STOP*
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${tot}')
print(f'Temos {milreais} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')