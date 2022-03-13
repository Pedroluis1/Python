num = int(input('\033[30;1;7mdigite um número\033[m: '))
resultado = num % 2
if resultado == 0:
    print('\033[30;7;1mo número é\033[m \033[33;1mpar\033[m')
else:
    print('\033[30;7;1mo número é\033[m \033[32;1mimpar\033[m')
