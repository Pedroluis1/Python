from time import sleep
from random import randint
import emoji

print(16 * '\033[34;1m-', 16 * '\033[31;1m-', 16 * '\033[33;1m-')
print(13 * '\033[34;1m-', 7 * '\033[31;1m-', '\033[34;1mJo\033[31mKen\033[33mPô\033[m', 7 * '\033[31;1m-',
      13 * '\033[33;1m-\033[m')
print(16 * '\033[34;1m-', 16 * '\033[31;1m-', 16 * '\033[33;1m-')
press = str(input('\033[32mPress enter for start\033[m'))
esc = int(input(emoji.emojize('\033[30mSuas opções:\033[m\n'
                              '\033[34m1\033[30m =\033[m :punch:(\033[34mpedra\033[m)\n'
                              '\033[31m2\033[30m =\033[m :raised_hand:(\033[31mpapel\033[m)\n'
                              '\033[33m3\033[30m =\033[m :v:(\033[33mtesoura\033[m)\n\033[30m:\033[m',
                              use_aliases=True)))
sleep(0.5)
print('\033[34;1mJO')
sleep(0.5)
print('\033[31;1mKEN')
sleep(0.5)
print('\033[33;1mPÔ\033[m')
sleep(0.5)
comp = (randint(1, 3))
if esc == 1 and comp == 1 or esc == 2 and comp == 2 or esc == 3 and comp == 3:
    print('\033[32mLoading...\033[m')
    sleep(1)
    print('\033[35mEmpate!\033[m')
elif esc == 1 and comp == 2 or comp == 1 and esc == 2:
    print('\033[32mLoading...\033[m')
    sleep(1)
    if esc == 1:
        print('\033[34mpedra\033[30m perde pra \033[31mpapel\033[30m.')
        print('\033[41mJogador perdeu!\033[m')
    elif esc == 2:
        print('\033[31mpapel\033[30m ganha da \033[34mpedra\033[30m.')
        print('\033[42mJogador venceu!!\033[m')
elif comp == 1 and esc == 3 or esc == 1 and comp == 3:
    print('\033[32mLoading...\033[m')
    sleep(1)
    if esc == 3:
        print('\033[33mtesoura\033[30m perde pra \033[34mpedra\033[30m.')
        print('\033[41mJogador perdeu!\033[m')
    elif esc == 1:
        print('\033[34mpedra\033[30m ganha de \033[33mtesoura\033[30m.')
        print('\033[42mJogador venceu!!\033[m')
elif comp == 2 and esc == 3 or esc == 2 and comp == 3:
    print('\033[32mLoading...\033[m')
    sleep(1)
    if esc == 2:
        print('\033[31mpapel\033[30m perde pra \033[33mtesoura\033[30m.')
        print('\033[41mJogador perdeu!\033[m')
    elif esc == 3:
        print('\033[33mtesoura\033[30m ganha de \033[31mpapel\033[30m.')
        print('\033[42mJogador ganhou!!\033[m')
else:
    print('\033[31;1mJogada inválida\033[m')
