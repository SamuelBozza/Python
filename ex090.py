'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela.
'''
registro = dict()
registro['nome'] = str(input('Nome: '))
registro['Média'] = float(input(f'Média de {registro["nome"]}:'))
print(f'Nome é igual a {registro["nome"]}')
print(f'Média é igual a {registro["Média"]}')
if registro['Média'] >= 7:
    print('Situação é igual a Aprovado')
elif registro['Média'] <= 7 and registro['Média'] >= 5:
    print('Situação é igual a Recuperação!')
else:
    print('Situação é igual a Reprovado')

