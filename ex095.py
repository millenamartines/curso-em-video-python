import emoji
time = []
jogador = {}
partidas = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print (emoji.emojize('\033[1;031m:x: ERRO! Responda apenas: S ou N. \033[m', use_aliases=True))
    if resp == 'N':
        break
print('-=' * 30)
print('\033[030mcod \033[m', end='')
for i in jogador.keys():
    print(f'\033[030m{i:<15}\033[m', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'\033[030m{k:>3} \033[m', end='')
    for d in v.values():
        print(f'\033[030m{str(d):<15}\033[m', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(emoji.emojize(f'\033[1;031m:x: ERRO! Não existe jogador com código {busca}!\033[m', use_aliases=True))
    else:
        print(f'\033[030m -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:\033[m')
        for i, g in enumerate(time[busca]['gols']):
            print(f'\033[030m No jogo {i+1} fez {g} gols.\033[m')
    print('-' * 40)
print('\033[030m<< VOLTE SEMPRE! >>\033[m')
