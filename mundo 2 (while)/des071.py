valor = int(input("informe o valor a ser sacado: R$"))
svalor = valor
while True:
    if valor % 2 != 0:
        print(f'O saque só poderá ser efetuado com a contia de \033[33m{svalor + 1}\033[m ou \033[34m{svalor - 1}\033[m.')
        nov = int(input('Qual opção será efetuada \033[33m(1°opção)\033[m ou \033[34m(2°opção)\033[m:'))
        if nov == 1:
            valor += + 1
            break
        elif nov == 2:
            valor += -1
            break
        else:
            print('Escolha uma alternativa proposta.')
    break
nota100 = valor // 100
valor %= 100
nota50 = valor // 50
valor %= 50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota2 = valor // 2
valor %= 2
if nota100 != 0:
    print(f'Total de {nota100} cédulas de R$100.')
if nota50 != 0:
    print(f'Total de {nota50} cédulas de R$50.')
if nota20 != 0:
    print(f'Total de {nota20} cédulas de R$20.')
if nota10 != 0:
    print(f'Total de {nota10} cédulas de R$10.')
if nota2 != 0:
    print(f'Total de {nota2} cédulas de R$2.')

# Ou pode ser dessa forma também, mas a primeira é melhor
"""valor = int(input('informe o valor a ser sacado: R$'))
total = valor
céd = 100
contcéd = 0
while True:
    if total >= céd:
        total -= céd
        contcéd += 1
    else:
        if contcéd > 0:
            print(f'Total de {contcéd} cédulas de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        contcéd = 0
        if total == 0:
            break"""
