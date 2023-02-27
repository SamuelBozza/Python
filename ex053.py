'''
CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS
'''
#ENTRADA DE DADOS
frase = str(input('Digite uma frase:')).strip().upper()
#DIVINDO A FRASE PARA LISTA
palavras = frase.split()
#JUNTANDO A FRASE À LISTA EM UMA STRING
junto = ''.join(palavras)
inverso = ''
#ESTRUTURA FOR
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')