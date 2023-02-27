import math
ângulo = int(input('Digite o ângulo que você deseja:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o seno de: {:.2f}!'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem o cosseno de: {:.2f}!'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print ('O ângulo de {} tem tangente de: {:.2f}!'.format(ângulo, tangente))