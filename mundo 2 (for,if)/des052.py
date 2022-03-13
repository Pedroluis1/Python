print(30 * '@', '\nDESCUBRA SE UM NÚMERO É PRIMO')
print(30 * '@')
primo = int(input('Digite um número: '))
tot = 0
for c in range(1, primo + 1):
    if primo % c == 0:
        print('\033[33;1m', end=' ')
        tot += 1
    else:
        print('\033[31;1m', end=' ')
    print(c, end=' ')
print(f'\n\033[34mO número \033[32;4m{primo}\033[m \033[34mfoi divisivel \033[32;4m{tot}\033[m \033[34mvezes.')
if tot == 2:
    print('\033[34mE por isso que ele é um número \033[32;1;4mprimo\033[m\033[34m!')
else:
    print('\033[34mE por isso que ele não é um número \033[31;1;4mprimo\033[m\033[34m!')
