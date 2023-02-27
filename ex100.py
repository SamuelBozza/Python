'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior.
'''
from random import randint
números = []

def sortear(sorte):
    print('Sorteando 5 valores da lista: ', end='')
    for sorteador in range(0,5):
        p = randint(0,10)
        números.append(p)
    print(f'{números} PRONTO!')

def somapares(soma):
    s = 0
    for sum in números:
        if sum % 2 == 0:
            s += sum
    print(f'Somando os valores pares de {números}, temos {s}')


sortear(1)
somapares(1)