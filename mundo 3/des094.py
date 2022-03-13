cadastro = dict()
lista = list()
idade = 0
mulheres = list()
idadeacim = list()
while True:
    cadastro['nome'] = str(input('nome: '))
    cadastro['sexo'] = str(input('sexo:M/F ')).lower()
    cadastro['idade'] = int(input('idade: '))
    lista.append(cadastro.copy())
    idade += cadastro['idade']
    idadeacim.append(cadastro['idade'])
    if cadastro['sexo'] == 'f':
        mulheres.append(cadastro['nome'])
    continuar = str(input('continuar:S/N ')).lower()
    if continuar == 'n':
        break
print(f'foram cadastradas {len(lista)} pessoas')
print(f'A média de idade do grupo é {idade / len(lista):.1f} anos')
if len(mulheres) > 0:
    print('As mulheres do grupo são: ',end='')
else:
    print('Não há mulheres no grupo')
for k, v in enumerate(mulheres):
    print(f'{v};', end='')
print('\nAs pessoas com idade acima da média são: ')
for k, v in enumerate(idadeacim):
    if v > idade / len(lista):
        print(f'    {lista[k]}')
