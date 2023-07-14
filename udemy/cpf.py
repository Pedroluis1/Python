from random import randint

def cpf():
    cont_regr = 10
    cpf_usuário = []
    digito = 0
    a = 9

    while True:
        for i in range (0,a):
            if a == 9:
                cpf_usuário.append(randint(0,9))
            digito += (cpf_usuário[i] * cont_regr)
            cont_regr -= 1
            if cont_regr == 1:
                digito *= 10
                digito %= 11
                digito = digito if digito <= 9 else 0
                cpf_usuário.append(digito)
                digito = 0
                if a == 10:
                    cont = 0
                    for item in range (0, 12):
                        if cont == 6 or cont == 3:
                            print(f'.{cpf_usuário[item]}',end='')
                        else:
                            print(cpf_usuário[item],end='')
                        cont += 1
                        if cont == 9:
                            break
                    print(f'-{cpf_usuário[9]}{cpf_usuário[10]}')
                    break
                a = 10
                cont_regr = 11


def validador (*num):
    cpf_usuário = ''.join(num)
    valida = []
    for item in cpf_usuário:
        valida.append(int(item))
    conf = [valida.pop(-2), valida.pop(-1)]

    cont_regr = 10
    digito = 0
    a = 9
    arm = []
    while True:
        for i in range (0,a):
            digito += (valida[i] * cont_regr)
            cont_regr -= 1
            if cont_regr == 1:
                digito *= 10
                digito %= 11
                digito = digito if digito <= 9 else 0
                arm.append(digito)
                valida.append(digito)
                digito = 0
                if a == 10:
                    if arm == conf:
                        return'cpf válido.'
                    else:
                        return 'cpf Inválido.'
                a = 10
                cont_regr = 11


def cpf_retorna():
    cont_regr = 10
    cpf_usuário = []
    digito = 0
    a = 9

    while True:
        for i in range (0,a):
            if a == 9:
                cpf_usuário.append(randint(0,9))
            digito += (cpf_usuário[i] * cont_regr)
            cont_regr -= 1
            if cont_regr == 1:
                digito *= 10
                digito %= 11
                digito = digito if digito <= 9 else 0
                cpf_usuário.append(digito)
                digito = 0
                if a == 10:
                    cpf_usuário = list(cpf_usuário)
                    cpf_usuário = str(cpf_usuário)
                    return cpf_usuário
                a = 10
                cont_regr = 11

print(cpf_retorna())
# cpf()
print(validador(f'{cpf_retorna()}'))


