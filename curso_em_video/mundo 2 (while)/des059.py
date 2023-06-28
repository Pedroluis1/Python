from time import sleep
pn = int(input('\033[35mPrimeiro número: \033[m'))
pn2 = int(input('\033[35mSegundo número: \033[m'))
while True:
    sleep(0.5)
    print(44 * '\033[31m-')
    opcao = int(input('\033[33m[1] \033[34msomar\033[m\n'
                      '\033[33m[2] \033[34mmultiplicar\033[m\n'
                      '\033[33m[3] \033[34mmaior\033[m\n'
                      '\033[33m[4] \033[34mnovos números\033[m\n'
                      '\033[33m[5] \033[34msair do programa\033[m\n:'))
    if opcao == 1:
        print(f'\033[35mA soma do número \033[33m{pn}\033[35m e \033[33m{pn2}\033[35m é \033[32m{pn + pn2}\033[35m.')
    elif opcao == 2:
        print(f'\033[35mA multiplicação dos números \033[33m{pn}\033[35m e \033[33m{pn2}\033[35m é \033[32m{pn * pn2}\033[35m.')
    elif opcao == 3:
        if pn > pn2:
            print(f'\033[35mO maior número é \033[32m{pn}\033[35m.')
        else:
            print(f'\033[35mO maior número é \033[32m{pn2}\033[35m.')
    elif opcao == 4:
        pn = int(input('\033[35mPrimeiro número: \033[m'))
        pn2 = int(input('\033[35mSegundo número: \033[m'))
    elif opcao == 5:
        break
