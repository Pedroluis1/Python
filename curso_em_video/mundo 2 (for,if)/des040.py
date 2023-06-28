print(15*" ",'\033[33;1mMédia = 7,00\033[m')
nota1 = float(input('\033[32;1mPrimeira nota:'))
nota2 = float(input('Segunda nota:\033[m'))
conc = (nota1 + nota2) / 2
if conc < 5:
    print(f'    \033[31;1;4mReprovado\033[m\n\033[30mNota = \033[31m{conc}\033[m')
elif conc >= 5 and conc <= 6.9:
    print(f'    \033[33;1;4mRecuperação\033[m\n\033[30mNota = \033[33m{conc}\033[m')
else:
    print(f'    \033[32;1;4mAprovado!\033[m\n\033[30mNota = \033[32m{conc}\033[m')
