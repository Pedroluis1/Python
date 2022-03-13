imp = []
par = []
lis = []
print('Digite 2020201 para, parar o programa.')
while True:
    list.append(int(input('Digite um número: ')))
    if list == 2020201:
        break
    if list % 2 == 0:
        par.append(list)
    else:
        imp.append(list)
print(30*'=-')
print(f'Pares: {par}')
print(f'Impares: {imp}')
print(f'lista: {lis}')
