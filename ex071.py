'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('='*30)
print('          BANCO CEV          ')
print('='*30)
valor = int(input('Que valor você quer sacar? R$')) #ENTRADA DO VALOR A SACAR
total = valor #VALOR PASSA A SER O TOTAL A SER SACADO.
céd = 50 #NOTA DE 50 REAIS
totcéd = 0 #QUANTIDADE DESSA MESMA NOTA
while True:
    # SE O VALOR A SACAR FOR MAIOR QUE 50 REAIS, ENTÃO O 'TOTAL' VAI TIRAR 50 REAIS(CÉD)
    # E A QUANTIA DESSA MESMA NOTA SOBE PARA 1, CASO O VALOR TOTAL AINDA SEJA MAIOR QUE A NOTA ATUAL (CÉD = 50) ELE IRA
    # REMOVER MAIS 50 REAIS E ADICIONAR MAIS 1 PARA O TOTAL DE NOTAS DE 50 SACADAS.
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0: #SE ALGUMA NOTA NÃO PRECISAR SER SACADA NENHUMA VEZ, NÃO APARECERA NO PRINT.
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50: #CASO NÃO CONSIGA REMOVER 50 REAIS DO VALOR ATUAL, A CÉD ATUAL PASSARA A SER 20.
            céd = 20
        elif céd == 20: #CASO NÃO CONSIGA REMOVER 20 REAIS DO VALOR ATUAL, A CÉD ATUAL PASSARA A SER 10.
            céd = 10
        elif céd == 10: #CASO NÃO CONSIGA REMOVER 10 REAIS DO VALOR ATUAL, A CÉD ATUAL PASSARA A SER 1.
            céd = 1
        totcéd = 0 #SOMA DE QUANTAS NOTAS DE CADA CÉDULA VÃO SER SACADAS.
        if total == 0: #QUANDO O VALOR TOTAL A SER SACADO ZERAR, O PROGRAMA ENCERRA.
            break
print('='*30)
print('Volte sempre ao Banco, tenha um bom dia!')
print('='*30)