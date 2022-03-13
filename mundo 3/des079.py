a = []
print('[para parar digite "-10101"]')
while True:
    b = int(input('Digite um valor: '))
    if b == -10101:
        break
    if b in a:
        print('valor duplicado. não vou adicionar...')
    else:
        a.append(b)
        a.sort()
print('todos os valores digitados em ordem:')
for c in a:
    print(f'{c} ', end='')
