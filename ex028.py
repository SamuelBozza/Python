import random

#entrada do número aleatorio gerado de 1 a 5.
numero = random.randint(1, 5)
#input para a tentativa de acerto do usuário.
t = int(input('Tente acertar o número gerado automáticamente pela máquina, numero esse de 1 a 5:'))
#resultado se o número escolhido pelo usuário for igual ao número gerado automáticamente.
if numero == t:
    print('Parabens! você acertou o número!')
else:
    print('Não foi dessa vez, tente na próxima!')