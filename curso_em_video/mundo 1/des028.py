from random import randint
from time import sleep

print(20 * '\033[1;33m-=-\033[m', '\n\033[34;1mvou pensar em um número de 0 a 5. Tente adivinhar...\033[m')
print(20 * '\033[1;33m-=-\033[m')
n = randint(0, 5)
n1 = int(input('Em que número eu pensei: '))
print('\033[35;1;1mPROCESSANDO...\033[m')
sleep(1.5)
if n1 == n:
    print('\033[32;1mPARÁBENS!!\033[32m \033[32mvocê consegui me vencer!!\033[m')
else:
    print(f'\033[31;1mGANHEI!!\033[m\033[31m eu pensei no número {n} e não no número {n1}')
