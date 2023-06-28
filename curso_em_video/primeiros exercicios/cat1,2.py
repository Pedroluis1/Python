import math,emoji
print('\033[34mTRIÂNGULO RETÂNGULO\033[m')
print(emoji.emojize('\033[33;1m:arrow_double_down:\033[m'*40, use_aliases=True))
cateto1=float(input('\033[31mDigite o comprimento do cateto oposto:\033[m '))
cateto2=float(input('\033[31mDigite o comprimento do cateto adjacente:\033[m '))
print(f'\033[34mA hypotenusa do triângulo retâgulo é: \033[30m{math.hypot(cateto1,cateto2):.2f}')