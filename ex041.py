'''
Até 9 anos = MIRIM
Até 14 anos = INFANTIL
Até 19 anos = JUNIOR
Até 25 anos = SÊNIOR
Acima: MASTER
'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento '))
idade = atual - nasc
print('O atleta  tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')

