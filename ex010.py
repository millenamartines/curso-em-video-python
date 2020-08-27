real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.48
euro = real / 6.15
iene = real / 19.56
print('Com R${:.2f} você pode comprar US${:.2f}, €{:.2f} e ¥{:.2f}'.format(real, dolar, euro, iene))

