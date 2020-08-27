n = int(input('\033[35mMe diga um número qualquer: \033[m'))
resultado = n % 2 #todo impar, a divisao por 2 = 1 e se par = 0
if resultado == 0:
    print('O número {} é \033[34mPAR\033[m'.format(n))
else:
    print('O número {} é \033[34mIMPAR\033[m'.format(n))
