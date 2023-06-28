conv = int(input('\033[35mescolha uma conversão:\033[31m\n'
                 '1-Binário\n'
                 '2-Octal\n'
                 '3-Hexadecimal\n\033[35m:'))
des = int(input('Digite o número desejado:'))
if conv == 1:
    print(f'\033[35mO número \033[31m{des} \033[35mBinário é\033[31m {bin(des)[2:]}')
elif conv == 2:
    print(f'\033[35mO número \033[31m{des} \033[35mOctal é\033[31m {oct(des)[2:]}')
elif conv == 3:
    print(f'\033[35mO número \033[31m{des} \033[35mHexadecimal é\033[31m {hex(des)[2:]}')
else:
    print('\033[33mDigite uma base de conversão válida')
