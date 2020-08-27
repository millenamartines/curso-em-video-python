def teste():
    x = 8    # Escopo local / Variável local
    print(f'Na função teste, n vale {n}.')
    print(f'Na função teste, x vale {x}.')


# Programa Principal
n = 2       # Escopo global / Variável global
print(f'No programa principal, n vale {n}.')
teste()
print(f'No programa principal, x vale {x}.')
