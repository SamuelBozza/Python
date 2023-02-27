s = input('Escreva algo:')
print('O tipo primitivo desse valor é:',type(s))
print('Só tem espaços?:{}'.format(s.isspace()))
print('É um número?:{}'.format(s.isnumeric()))
print('É alfabético?:{}'.format(s.isalpha()))
print('É um número alphanúmerico?:{}'.format(s.isalnum()))
print('Esta em maiúsculo?:{}'.format(s.isupper()))
print('Esta em minúsculo?:{}'.format(s.islower()))
print('É capitalizado?:{}'.format(s.istitle()))


