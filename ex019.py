'''import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro anluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]   #lista sempre em []
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''


from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro anluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]   #lista sempre em []
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))