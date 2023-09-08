# ordenando de outras formas
lista = [
    {'nome': 'Luiz', 'Sobrenome': 'mirana'},
    {'nome': 'Ana', 'Sobrenome': 'Paula'},
    {'nome': 'Pedro', 'Sobrenome': 'Luís'},
    {'nome': 'Aruan', 'Sobrenome': 'vasconcelas'},
    {'nome': 'Brenda', 'Sobrenome': 'faria'}
]

'''def ordena (item):
    return item['nome']
lista.sort(key=ordena)'''# ou 

lista.sort(key=lambda item: item['nome']) # mexe na ordem da sua lista

for item in lista:
    print(item)

#-----------------------------------

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])  #cópia rasa
l2 = sorted(lista, key=lambda item: item['Sobrenome'])
# lambda aula 134