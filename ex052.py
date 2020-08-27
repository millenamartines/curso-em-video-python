num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele \33[33mÉ PRIMO!')
else:
    print('Por isso ele \33[31mNÃO É PRIMO!')