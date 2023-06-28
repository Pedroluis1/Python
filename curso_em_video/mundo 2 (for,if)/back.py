valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    y = input('deseja continuar? s/n ')
    if y != 's'or'S':
        break
    else:
        while True:
            valores.append(int(input('Digite um valor: ')))
            y = input('deseja continuar? s/n ')

