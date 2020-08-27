from random import randint
from time import sleep
lista = list()
jogos = list()
print('\033[033m-' * 40)
print(f'\033[030m{"JOGA NA MEGA SENA":^40}\033[m')
print('\033[033m-\033[m' * 40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('\033[033m--=\033[m' * 3, f' \033[030mSORTEANDO {quant} JOGOS\033[m ', '\033[033m--=\033[m' * 3)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('\033[033m--=\033[m' * 3, ' \033[030mBOA SORTE!\033[m ', '\033[033m--=\033[m' * 3)
