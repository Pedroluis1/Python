num1 = int(input('\033[35;4mPrimeiro Valor\033[m: '))
num2 = int(input('\033[35;4mSegundo Valor\033[m: '))
num3 = int(input('\033[35;4mTerceiro Valor\033[m: '))
valores = num1,num2,num3
print(f'\033[33mO maior valor digitado foi \033[m{max(valores)}')
print(f'\033[33mO menor valor digititado foi \033[m{min(valores)} ')