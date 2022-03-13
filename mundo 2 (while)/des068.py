from random import randint

print(10 * '\033[31m=-', '\n\033[33mPar ou Impar')
print(10 * '\033[31m=-\033[m')
cont = -1
while True:
    comp = randint(1, 10)
    player = str(input('\033[35mPar ou Impar? P/I \033[m'))
    num = int(input('\033[35mDigite seu número: \033[m'))
    cont += 1
    soma = num + comp
    if soma % 2 == 0:
        if player in 'Pp':
            print(f'\033[33mVocê jogou \033[34;4m{num}\033[m \033[33me o computador \033[34;4m{comp}\033[m\033[33m\0.'
                  f'\033[33mtotal deu \033[32;4m{comp + num} Par\033[m\033[33m.\n'
                  f'\033[32mVocê ganhou!!\033[m \033[33mParabéns.\033[m')
        elif player in 'Ii':
            print(f'\033[33mVocê jogou \033[34;4m{num}\033[m \033[33me o computador \033[34;4m{comp}\033[m\033[33m\0.'
                  f'\033[33mtotal deu \033[31;4m{comp + num} Par\033[m\033[33m.\n'
                  f'\033[31mVocê Perdeu!!\033[m')
            print(f'\033[31;1mGAME OVER\033[m\033[35m, você venceu {cont} vezes.\033[m')
            break
    elif soma % 2 != 0:
        if player in 'Pp':
            print(f'\033[33mVocê jogou \033[34;4m{num}\033[m \033[33me o computador \033[34;4m{comp}\033[m\033[33m\0.'
                  f'\033[33mtotal deu \033[31;4m{comp + num} Impar\033[m\033[33m.\n'
                  f'\033[31mVocê Perdeu!!\033[m')
            print(f'\033[31;1mGAME OVER\033[m\033[35m, você venceu {cont} vezes.\033[m')
            break
        elif player in 'Ii':
            print(f'\033[33mVocê jogou \033[34;4m{num}\033[m \033[33me o computador \033[34;4m{comp}\033[m\033[33m\0.'
                  f'\033[33mtotal deu \033[32;4m{comp + num} Impar\033[m\033[33m.\n'
                  f'\033[32mVocê ganhou!!\033[m \033[33mParabéns.\033[m')
