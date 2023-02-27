'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
print('Gerador de PA')
print('-='*10)
#ENTRADA DE DADOS
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
#DEFININDO
cont = 1
total = 0
mais = 10
#ESTRUTURA WHILE
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))