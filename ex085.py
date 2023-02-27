'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
princ = list()
par = list()
impar = list()
for v in range(1,8):
    princ.append(int(input(f'Digite o {v}o. valor: ')))
for valor in princ:
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
princ.clear()
print('-='*27)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores ímpares digitados foram: {sorted(impar)}')
print('-='*27)