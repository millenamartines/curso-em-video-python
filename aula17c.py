'''a = [2, 3, 4, 7]
b = a
b[2] = 8     # altera as 2 listas. Faz uma ligação das listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''


a = [2, 3, 4, 7]
b = a[:]    # Cópia dos valores de a para b
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
