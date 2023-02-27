#entrada de dados
salario = int(input('Entre com seu salário para saber seu aumento:'))

if salario <= 1250:
    print('O seu novo salario tera um aumento de {:.2f}'.format(salario*15/100+salario))
else:
    print('O seu novo salario tera um aumento de {:.2f}'.format(salario*10/100+salario))