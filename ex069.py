'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''
print('-'*26)
print('   CADASTRE UMA PESSOA   ')
print('-'*26)
pessoa_maioridade = qntd_homens = idade_mulher = idade = 0 #DEFINIÇÕES PARA 0
while True:
    idade = int(input('Idade: ')) #ENTRADA DE IDADE
    sexo = ' '
    c = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()[0].strip() #ENTRADA DE SEXO
    while c not in 'SN':
        c = str(input('Quer continuar? [S/N] ')).upper()[0].strip() #OPÇÕES DE CONTINUIDADE
    if idade >= 18: #CONTADOR DE PESSOAS MAIORES DE 18 ANOS
        pessoa_maioridade += 1
    if sexo == 'M': #CONTADOR DE HOMENS
        qntd_homens += 1
    if sexo == 'F' and idade < 20: #CONTADOR DE MULHERES COM MENOS DE 20 ANOS
        idade_mulher += 1
    if c == 'N': #ESTRUTURA PARA PARAR.
        break
print(f'Total de pessoas com mais de 18 anos: {pessoa_maioridade}!')
print(f'Ao todo temos {qntd_homens} homens cadastrados!')
print(f'E temos {idade_mulher} mulheres com menos de 20 anos!')