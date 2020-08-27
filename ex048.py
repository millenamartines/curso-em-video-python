'''
Soma entre todos os numeros impares que são
multiplos de 3 e que se encontram no
intervalo de 1 ate 500.
'''

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += + c
        cont += + 1
print('A soma de todos os {} valores solicitados é: {}'.format(cont, soma))
