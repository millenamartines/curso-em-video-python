'''import math
#val = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(val, math.trunc(val)))
                     #ou
from math import trunc
val = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(val, trunc(val)))'''

val = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira foi {}'.format(val, int(val)))