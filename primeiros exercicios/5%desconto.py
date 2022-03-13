d = float(input('\033[30mpreço:\033[32mR$'))
print(f'\033[33;1mDesconto \033[32;4;1m5%\033[m \033[33mé igual a \033[32;4;1m'
      f'{d - d * 0.05 }\033[m \033[33;1mreais')
