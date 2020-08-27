prod = float(input('Qual o valor do produto? R$'))
vista = prod - (prod * 10 / 100)
prazo = prod + (prod * 8 / 100)
print('O valor do produto é R${:.2f}'.format(prod))
print('O valor deste produto a vista é R${:.2f}'.format(vista))
print('O valor deste produto parcelado é R${:.2f}'.format(prazo))


