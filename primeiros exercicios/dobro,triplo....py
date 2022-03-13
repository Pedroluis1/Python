n = int(input('\033[30;7mDigite um número:\033[m '))
print(f'\033[30mO dobro de\033[31m {n}\033[30m é \033[33m{n*2}\n\033[30mO triplo de \033[31m{n} \033[30mé\033[33m {n*3}\n'
      f'\033[30mA raiz quadrada de \033[31m{n}\033[30m é \033[34m{n**(1/2):.3f}')