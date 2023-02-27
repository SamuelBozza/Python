'''
ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERA
A BASE DE CONVERSÇÃO: -1 PARA BINÁRIO;-2 PARA OCTAL;-3 PARA HEXADECIMAL.
'''
#ENTRADA DOS DADOS.
n = int(input('Digite um número inteiro:'))
#INPUT PERGUNTANDO QUAL CONVERSÃO O USUÁRIO DESEJA.
convert = int(input('O número gerado foi:{} \n'
                    '[ 1 ] para Binário \n'
                    '[ 2 ] para Octal \n'
                    '[ 3 ] para hexadecimal \n'
                    'Qual sera a base de conversção?:'.format(n)))
#CONVERSÕES.
if convert == 1:
    x = bin(n)
    print(x[2::])
elif convert == 2:
    x2 = oct(n)
    print(x2[2::])
else:
    x3 = hex(n)
    print(x3[2::])

