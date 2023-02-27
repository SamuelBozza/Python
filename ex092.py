'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from date import datetime
registro = {}
registro_0 = list()
while True:
    registro['nome'] = str(input('Nome: '))
    ano = int(input('Ano de nascimento: '))
    registro['idade'] = datetime.now().year - ano
    registro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    registro_0.append(registro.copy())
    if registro['ctps'] == 0:
        for reg in registro_0:
            for k, v in reg.items():
                print(f'{k} tem o valor {v}')
        break
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = int(input('Salário: R$ '))
    cont = datetime.now().year - registro['contratação']
    cont1 = 35 - cont
    registro['aposentadoria'] = registro['idade'] + cont1
    if registro['ctps'] > 0:
        for k, v in registro.items():
            print(f'{k} tem o valor {v}')
        break