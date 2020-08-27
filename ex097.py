def escreva(msg):
    tam = len(msg) + 4     # coloca 2 linhas antes e 2 depois
    print('~' * tam)
    print(f'  {msg}')      # dar 2 espaços
    print('~' * tam)



# Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
