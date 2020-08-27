nome = str(input('Digite o seu nome completo: ')).strip()   #strip elimina espacos atntes e dps
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras '.format(len(nome)-nome.count(' ')))   #count conta e dentro qts espacos
#print('Seu primeiro nome é ele tem {} letras'.format(nome.find(' '))) #conta o primeiro
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
