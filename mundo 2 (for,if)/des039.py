from datetime import date
from time import sleep
sexo = int(input('\033[30minforme seu sexo:\033[m\n\033[34m1-masculino\n\033[35m2-Feminino\033[30m\n:\033[m'))
if sexo == 1:
    ano = int(input('\033[32mDigite o ano de seu nascimento: '))
    mes = int(input('mês:\033[m '))
    tm = 12 - date.today().month + mes
    tn = 18 - date.today().year + ano-1
    if tm >= 12:
        tn = 18 - date.today().year + ano-1 +1
        tm = 12 - date.today().month + mes -12
    print('\033[32;1mProcessing...\033[m')
    sleep(1)
# já passou da hora.
    if date.today().year - ano > 18:
        print(f'\033[31mjá passou da hora de se alistar.\033[m\n'
              f'\033[33mVocê deveria ter se alistado em \033[34;4m{ano+18}\033[m')
# está na hora.
    elif date.today().year - ano == 18:
        print(f'\033[33mEstá na hora de se alistar.\033[m\n')
# ainda terá.
    else:
        print('\033[33mvocê ainda terá que se alistar.\033[33m')
        if tm == 0:
            print(f'\033[33mDaqui \033[34;4m{tn}\033[m \033[33mano')
        if tn == 0:
                print(f'\033[33mEm \033[34;4m{tm}\033[m \033[33mmeses.')
        else:
            if tn ==1 and tm==1:
                print(f'\033[33mDaqui \033[34;4m{tn}\033[m \033[33mano e \033[34;4m{tm}\033[m \033[33mmês.')
            elif tn == 1 and tn != 0 and tm !=0:
                print(f'\033[33mDaqui \033[34;4m{tn}\033[m \033[33mano',end='')
                if tm>=2:
                    print(f' e \033[34;4m{tm}\033[m \033[33mmeses.')
                if tm ==1 and tm !=0:
                    print(f'\033[34;4m{tm}\033[m \033[33mmês.')
elif sexo == 2:
    print('\033[32mVocê não precisa fazer alistamento militar obrigatório.\033[m')
else:
    print('\033[31;1mERRO\n\033[31mDigite um valor válido!')
