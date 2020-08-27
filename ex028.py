from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[33m-=-' * 20)
print('\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[33m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? '))
print('\033[35mPROCESSANDO...')
sleep(1)
if computador == jogador:
    print('\033[33mPARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31mGANHEI! Eu pensei no múmero {} e não no {}!'.format(computador, jogador))
