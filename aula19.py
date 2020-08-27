pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
#del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')


'''for k in pessoas.values():
    print(k)'''

'''for k in pessoas.keys():
    print(k)'''

#print(pessoas.items())
#print(pessoas.values())
#print(pessoas.keys())
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
