'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
#entrada de dados
sexo =str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
#estrutura while
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
#prints
print('Sexo {} registrado com sucesso!'.format(sexo))