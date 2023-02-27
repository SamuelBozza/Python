'''
REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
-EQUILÁTERO: TODOS OS LADOS IGUAIS
-ISÓSCELES: DOIS LADOS IGUAIS
-ESCALENO: TODOS OS LADOS DIFERENTES
'''
#ENTRADA DE DADOS
reta1 = float(input('Entre com o comprimento da primeira reta:'))
reta2 = float(input('Entre com o comprimento da segunda reta:'))
reta3 = float(input('Entre com o comprimento da terceira reta:'))
#TRANSFORMANDO EM TIPOS DE TRIÂNGULOS
if reta1 == reta2 == reta3:
    print('Esse é um triângulo \033[1;30;41mEQUILÁTERO\033[m')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print('Esse é um triângulo \033[1;30;41mISÓSCELES\033[m')
else:
    print('Esse é um triângulo \033[1;30;41mEscaleno\033[m')
