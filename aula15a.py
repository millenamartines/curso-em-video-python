nome = 'José'
idade = 33
salário = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}.') #PYTHON 3.6+
print('O {} tem {} anos e ganha R${:.2f}.'.format(nome, idade, salário)) #PYTHON 3
print('O %s tem %d anos e ganha R$%.2f.' % (nome, idade, salário))  #PYTHON 2

