'''
A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E
MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
-ATÉ 9 ANOS: MIRIM
-ATÉ 14 ANOS: INFANTIL
-ATÉ 19 ANOS: JUNIOR
-ATÉ 20 ANOS:SÊNIOR
-ACIMA: MASTER
'''
#IMPORTAÇÕES
from datetime import date
#DADOS DA DATA ATUAL *ANO*
data_atual = date.today()
ano_atual:int = data_atual.year
#NASCIMENTO DO USUÁRIO.
nascimento = int(input('Qual seu ano de nascimento?:'))
#CALCULAR IDADE.
idade = ano_atual - nascimento
#CONVERTENDO AS IDADES PARA AS CATEGORIAS.
if idade < 9:
    print('Com {} anos, sua categoria é: MIRIM!'.format(idade))
elif idade > 9 and idade < 14:
    print('Com {} anos, sua categoria é: INFANTIL!'.format(idade))
elif idade > 14 and idade < 19:
    print('Com {} anos, sua categoria é JUNIOR!'.format(idade))
elif idade == 20:
    print('Com 20 anos, sua categoria é SÊNIOR!')
else:
    print('Com idade acima de 20 anos, sua categoria é MASTER!')
