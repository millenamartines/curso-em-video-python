# carro custa R$60,00 por dia
# valor de R$0.15 por Km rodado
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pagar = (dias * 60.00) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pagar))

