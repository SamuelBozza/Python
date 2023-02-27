'''
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
'''
quantidade = soma = 0 #DEFININDO A QUANTIDADE DE NÚMERO PARA SOMA E SOMA PARA 0
while True:
    núm = int(input('Digite um valor (999 para parar): ')) #ENTRADA DE DADOS
    if núm == 999: #CONDIÇÃO DE PARADA
        break
    soma += núm #SOMANDO OS NÚMEROS
    quantidade += 1  # ADICIONANDO +1 Á QUANTIDADE TODA VEZ QUE A ESTRUTURA WHILE FOR REINICIADA.
print(f'A soma dos {quantidade} valores foi: {soma}')
