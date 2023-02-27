'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''
def área(larg, comp):
    soma = larg * comp
    print(f'O tamanho da área de largura {larg} e comprimento {comp} é {soma}m²')


print('CALCULANDO ÁREA')
print('-'*20)
l = float(input('Digite o tamanho da largura em metros: '))
c = float(input('Digite o tamanho do comprimento em metros: '))
área(l, c)