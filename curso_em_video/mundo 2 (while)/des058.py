from random import randint
from time import sleep

print(20 * '\033[1;33m-=-\033[m', '\n\033[34;1mvou pensar em um número de 1 a 10. Tente adivinhar...\033[m')
print(20 * '\033[1;33m-=-\033[m')
n = randint(1, 10)
n1 = int(input('\033[34mEm que número eu pensei:\033[m '))
print('\033[35;1;1mPROCESSANDO...\033[m')
sleep(1)
cont = 0
while not n == n1:
    print('\033[31merrou!\033[m')
    if n > n1:
        print('\033[34mmais...\033[m')
    elif n < n1:
        print('\033[34mmenos...\033[m')
    n1 = int(input('\033[33mtente mais uma vez: \033[m'))
    print('\033[35;1;1mPROCESSANDO...\033[m')
    sleep(1)
    cont += 1
if cont == 0:
    print(f'\033[32;1mPARÁBENS!!\033[32m \033[32mvocê acertou\nDe primeira.\033[33m')
elif n1 == n:
    print(
        f'\033[32;1mPARÁBENS!!\033[32m \033[32mvocê acertou\033[33m, mas precisou de \033[31m{cont+1}\033[33m tentativas.\033[m')
