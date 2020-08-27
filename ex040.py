'''
Média abaixo de 5.0: REPROVADO
Média entre 5.0 e 6.9: RECUPERAÇÃO
Média 7.0 ou superior: Aprovado
'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))
if 7 > m >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif m < 5:
    print('O aluno está REPROVADO')
elif m >= 7:
    print('O aluno está APROVADO')
