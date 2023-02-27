'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
maior = menor = 0
temp = []
princ = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    op = str(input('Deseja continuar?: [S/N] '))
    if op in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Pesso de', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}Kg. Pesso de', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()