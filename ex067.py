'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    print('-' * 37)
    c = int(input('Quer ver a tábuada de qual valor?: ')) #ENTRADA DE DADOS.
    print('-' * 37)
    if c < 0: #DEFININDO O BREAK CASO UM NÚMERO NEGATIVO SEJA INSERIDO.
        break
    for números in range(1,11):
        print(f'{c} x {números} = {c*números}')
print('Programa de tábuada encerrado, volte sempre!')