# Tuplas são imutáveis

lanche = ('Coca', 'Sopa', 'Mousse', 'Pizza')

#for cont in range(0, len(lanche)):
#    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

#   print(lanche[cont])


#for comida in lanche:
#    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')
