from datetime import date

nasc = int(input('\033[32;1minforme o ano da sua data de nascimento: \033[m'))
idade = date.today().year - nasc
if idade <= 9:
    print(f'\033[33;1mSua categoria é a Mirim.\n\033[32;1mCom {idade} anos.\033[m')
elif idade <= 14:
    print(f'\033[33;1mSua categoria é a Infantil.\n\033[32;1mCom {idade} anos.\033[m')
elif idade <= 19:
    print(f'\033[33;1mSua categoria é a Junior.\n\033[32;1mCom {idade} anos.\033[m')
elif idade == 20:
    print(f'\033[33;1mSua categoria é a Sênior.\n\033[32;1mCom {idade} anos.\033[m')
else:
    print(f'\033[33;1mSua categoria é a Master.\n\033[32;1mCom {idade} anos.\033[m')
