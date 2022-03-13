temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi {mai}Kg de', end='')
for p in princ:
    if p[1] == mai:
        print(f'{[p[0]]}', end='')
print(f'E o menor peso foi {men} de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{[p[0]]}', end='')
