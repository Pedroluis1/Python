while True:
    numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', \
              'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
    esc = int(input('\033[35mDigite um número entre \033[33m0 e 20\033[35m: '))
    while esc > 20 or esc < 0:
        esc = int(input('\033[31mTente novamente.\033[35mDigite um número entre \033[33m0 e 20\033[35m: '))
    print(f'\033[35mVocê digitou o número \033[33m{numeros[esc]}')
    qr = str(input('\033[35mQuer que continue? \033[33mS/N ')).strip().upper()
    if qr in 'N':
        break
