pr = float(input('\033[30mValor do produto:\033[32mR$\033[m'))
pg = int(input('\033[30mForma de pagamento:\033[m '
               '\n\033[4;31m1\033[m- \033[30mÁ vista \033[34;1mdinheiro/cheque\033[m\033[30m:\033[35;1m10%\033[m\033[30m de desconto\n'
               '\033[4;32m2\033[m- \033[30mÁ vista no \033[34;1mcartão\033[m\033[30m:\033[35;1m5%\033[m\033[30m de desconto\n'
               '\033[4;33m3\033[m- \033[30mEm até 2x no \033[34;1mcartão\033[m\033[30m: preço normal\n'
               '\033[4;34m4\033[m- \033[30m3x ou mais no \033[34;1mcartão\033[m\033[30m: \033[35;1m20%\033[m\033[30m de juros\n'
               '\033[30;1mDigite o valor, de acordo com a forma de pagamento escolhido:\033[m '))
# primeira forma
if pg == 1:
    print('\033[30mA forma de pagamento escolhida foi\033[m '
          '\033[30má vista \033[34;1mdinheiro/cheque\033[m\033[30m:\033[35;1m10%\033[m\033[30m de desconto?')
    confir = int(input('\033[32;1m1 CONFIRMAR\n\033[31;1m2 CANCELAR\033[m\n\033[30m:\033[m'))
    if confir == 1:
        print(
            f'\033[30mForma de pagamento \033[32;1mconfirmada\033[m\033[30m!\033[m\n\033[30mO valor será de \033[32mR${pr - pr * 0.10}\033[m')
    elif confir == 2:
        print('\033[30mOperação \033[31;1;4mcancelada!')
    else:
        print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
# Segunda forma
elif pg == 2:
    print('\033[30mA forma de paganeto escolhida foi \033[m'
          '\033[30má vista no \033[34;1mcartão\033[m\033[30m:\033[35;1m5%\033[m\033[30m de desconto?')
    confir = int(input('\033[32;1m1 CONFIRMAR\n\033[31;1m2 CANCELAR\033[m\n\033[30m:\033[m'))
    if confir == 1:
        print(
            f'\033[30mForma de pagamento \033[32;1mconfirmada\033[m\033[30m!\033[m\n\033[30mO valor será de \033[32mR${pr - pr * 0.05}\033[m')
    elif confir == 2:
        print('\033[30mOperação \033[31;1;4mcancelada!')
    else:
        print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
# Terceira forma
elif pg == 3:
    print('\033[30mA forma de pagamento escolhida foi\033[m '
          '\033[30mem até 2x no \033[34;1mcartão\033[m\033[30m: preço normal?')
    confir = int(input('\033[32;1m1 CONFIRMAR\n\033[31;1m2 CANCELAR\033[m\n\033[30m:\033[m'))
    if confir == 1:
        print(
            f'\033[30mForma de pagamento \033[32;1mconfirmada\033[m\033[30m!\033[m\n\033[30mO valor será de \033[32mR${pr}\033[m\n'
            f'\033[32mR${pr / 2 :.2f}\033[30m por \033[33m2 \033[30mmeses.\033[m')
        fin = int(input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
        if fin == 1:
            print('\033[32;1mOperação \033[4mfinalizada!\033[m')
        elif fin == 2:
            print('\033[31;1mOperação \033[4mcancelada!\033[m')
        else:
            print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
            fin = int(input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
            if fin == 1:
                print('\033[32;1mOperação \033[4mfinalizada!\033[m')
            elif fin == 2:
                print('\033[31;1mOperação \033[4mcancelada!\033[m')
            else:
                print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!!!')
                fin = int(
                    input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
                if fin == 1:
                    print('\033[32;1mOperação \033[4mfinalizada!\033[m')
                elif fin == 2:
                    print('\033[31;1mOperação \033[4mcancelada!\033[m')
                else:
                    print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!!!!')
    elif confir == 2:
        print('\033[30mOperação \033[31;1;4mcancelada!')
    else:
        print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
# Quarta forma
elif pg == 4:
    print('\033[30mA forma de pagamento escolhida foi\033[m '
          '\033[30m3x ou mais no \033[34;1mcartão\033[m\033[30m: \033[35;1m20%\033[m\033[30m de juros?')
    confir = int(input('\033[32;1m1 CONFIRMAR\n\033[31;1m2 CANCELAR\033[m\n\033[30m:\033[m'))
    if confir == 1:
        print(f'\033[30mForma de pagamento \033[32;1mconfirmada\033[m\033[30m!\033[m')
        parcelas = int(input('\033[30mQuantas parcelas? \033[m'))
        if parcelas < 3:
            print('\033[31mO número de parcelas não está incluído na forma de pagamento escolhida\033[30m.\n'
                  '\033[33mEscolha outra forma de pagamento ou mude o número de parcelas\033[30m.\033[m')
        elif parcelas <= 12:
            print(
                f'\033[30mO valor será de \033[32mR${pr * 0.20 + pr}\033[30m parcelado em \033[33m{parcelas}x\033[30m.\n'
                f'\033[32mR${pr / parcelas:.2f}\033[30m por \033[33m{parcelas} \033[30mmeses.\033[m')
            fin = int(input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
            if fin == 1:
                print('\033[32;1mOperação \033[4mfinalizada!\033[m')
            elif fin == 2:
                print('\033[31;1mOperação \033[4mcancelada!\033[m')
            else:
                print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
                fin = int(
                    input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
                if fin == 1:
                    print('\033[32;1mOperação \033[4mfinalizada!\033[m')
                elif fin == 2:
                    print('\033[31;1mOperação \033[4mcancelada!\033[m')
                else:
                    print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!!!')
                    fin = int(
                        input('\033[32;1m1 Finalizar a Operação\n\033[31;1m2 Cancelar Operação\033[m\n\033[30m:\033[m'))
                    if fin == 1:
                        print('\033[32;1mOperação \033[4mfinalizada!\033[m')
                    elif fin == 2:
                        print('\033[31;1mOperação \033[4mcancelada!\033[m')
                    else:
                        print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!!!!')
        else:
            print('\033[31mO número de parcelas excedeu o limite que é \033[30m12x.\033[m')
    elif confir == 2:
        print('\033[30mOperação \033[31;1;4mcancelada!')
    else:
        print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
else:
    print('\033[31;1mERRO!\n\033[m\033[31mDigite um valor válido!')
