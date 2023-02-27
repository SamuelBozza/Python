'''
CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO
UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
-MÉDIA ABAIXO DE 5.0: REPROVADO.
-MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO.
-MÉDIA 7.0 OU SUPERIOR: APROVADO.
'''
#ENTRADA DOS DADOS.
nota1 = float(input('Sua primeira nota?:'))
nota2 = float(input('Sua segunda nota?:'))
#CALCULANDO MÉDIA.
media = (nota1+nota2)/2
#RESULTADOS FINAIS.
if media < 5.0:
    print('\033[1;31;40mREPROVADO!\033[m')
elif media < 6.9 and media > 5.0:
    print('\033[1;33;40mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32;40mAPROVADO!\033[m')