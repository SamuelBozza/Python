'''
DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO
COM A TABELA A BAIXO:
-ABAIXO DE 18.5:ABAIXO DO PESO
-ENTRE 18.5 E 25:PESO IDEAL
-25 ATÉ 30:SOBREPESO
-30 ATÉ 40: OBESIDADE
-ACIMA DE 40: OBESIDADE MÓRBIDA
'''
#ENTRADA DE DADOS
Peso = float(input('Entre com seu Peso:'))
Altura = float(input('Entre com sua Altura:'))
#CALCULO IMC
IMC = Peso/Altura**2
#CONVERTENDO O IMC PARA ESTRTURA IF/ELIF
if IMC < 18.5:
    print('Com um IMC de {:.1f}, Você está abaixo do Peso!'.format(IMC))
elif IMC > 18.5 and IMC < 25:
    print('Com um IMC de {:.1f}, Você está com o Peso ideal!'.format(IMC))
elif IMC > 25 and IMC < 30:
    print('Com um IMC de {:.1f}, Você está Sobrepeso!'.format(IMC))
elif IMC > 30 and IMC < 40:
    print('Com um IMC de {:.1f}, Você está com Obesidade!'.format(IMC))
else:
    print('Com um IMC de {:.2f}, Você está com Obesidade Mórbida!'.format(IMC))


