sal = float(input('\033[33mDigite seu salário: R$\033[m'))
if sal <=1250.00:
    print(f'\033[33mSeu salário com o aumento\033[m: \033[32;1mR${sal*0.15+sal:.2f}\033[m')
else:
    print(f'\033[33mseu salário com o aumento\033[m: \033[32;1mR${sal*0.1+sal:.2f}\033[m')