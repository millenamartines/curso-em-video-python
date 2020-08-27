'''
Salário superior a R$1.250,00  = aumento  10%
Salários inferiores ou iguais = aumento 15%
'''

sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, novo))
