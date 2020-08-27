from random import randint
import emoji
v = 0
print('\033[1;033m=-' * 15, '\033[m')
print('\033[1;030mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[1;033m=-' * 15, '\033[m')
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print(emoji.emojize('PARABÉNS! Você venceu! :smiley: ', use_aliases=True))
            v += 1
        else:
            print(emoji.emojize('Você perdeu :disappointed:', use_aliases=True))
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print(emoji.emojize('PARABÉNS! Você venceu! :smiley:', use_aliases=True))
            v += 1
        else:
            print(emoji.emojize('Você perdeu :disappointed:', use_aliases=True))
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')
