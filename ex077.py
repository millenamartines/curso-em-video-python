palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')  # para ficar em maiusculas: {p.upper()}
    for letra in p:
        if letra.lower() in 'aeiou':             #'aáãâeéêiíoóôõuú'
            print(letra, end=' ')
