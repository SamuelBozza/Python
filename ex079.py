'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.
'''
list = []
while True:
    n = int(input('Digite um número: '))
    if n not in list:
        list.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado e descartado!')
    op = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if op in 'Nn':
        break
print('-='*30)
list.sort()
print(f'Você digitou os valores {list}')