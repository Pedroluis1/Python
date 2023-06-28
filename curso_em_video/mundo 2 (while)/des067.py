while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(36 * '-')
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c}x{n}={c * n}')
    print(20 * '-')
    ok = str(input('Quer continuar?S/N '))
    if ok in 'Nn':
        print(20 * '-')
        break
print('Programa tabuada encerrado, volte sempre!')
