'''
R$0.50 por km para viagens até 200km
R$0.45 para viagens mais longas
'''

dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(dist))

'''if dist <= 200:
    preco = dist * 0.50
else:
    preco = dist * 0.45'''
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
