pnum = int(input('\033[33mPrimeiro número:'))
snum = int(input('Segundo número:\033[m'))
if pnum > snum:
    print('\033[33mO \033[34;4mprimeiro\033[m\033[33m valor é maior!')
elif snum > pnum:
    print('\033[33mO \033[34;4msegundo\033[m\033[33m valor é maior!')
else:
    print('\033[33mNão existe valor maior, os dois são \033[34;4miguais\033[m\033[33m!')
