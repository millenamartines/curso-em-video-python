a = input('Digite algo: ')  # a = objeto
print('O tipo primitivo deste valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É só um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

# os islower, isnumeric... são métodos