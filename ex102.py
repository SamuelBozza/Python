'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.
'''
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (OPCIONAL) Mostrar ou não a conta.
    :return: O valor da Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(5))
#help(fatorial)
e = int(input('Qual fatorial deseja ver?: '))
while True:
    t = str(input('Deseja ver o calculo do fatorial? [T/F]'))
    if t not in 'TtFf':
        print('Não entendi, por favor utilize apenas [T/F]')
    elif t in 'TtFf':
        if t in 'Ff':
            print(fatorial(e))
            break
        else:
            print(fatorial(e, show=True))
            break