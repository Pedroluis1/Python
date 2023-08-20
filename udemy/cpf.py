from random import randint

def cpf():
    cont_regr = 10
    cpf_usuario = []
    digito = 0
    a = 9

    while True:
        for i in range (0,a):
            if a == 9:
                cpf_usuario.append(randint(0,9))
            digito += (cpf_usuario[i] * cont_regr)
            cont_regr -= 1
            if cont_regr == 1:
                digito *= 10
                digito %= 11
                digito = digito if digito <= 9 else 0
                cpf_usuario.append(digito)
                digito = 0
                if a == 10:
                    cont = 0
                    for item in range (0, 12):
                        if cont == 6 or cont == 3:
                            print(f'.{cpf_usuario[item]}',end='')
                        else:
                            print(cpf_usuario[item],end='')
                        cont += 1
                        if cont == 9:
                            break
                    print(f'-{cpf_usuario[9]}{cpf_usuario[10]}')
                    break
                a = 10
                cont_regr = 11


def validador (*num):
    cpf_usuario = ''.join(num)
    valida = []
    for item in cpf_usuario:
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
    cpf_usuario = ""
    digito = 0
    a = 9

    while True:
        for i in range(a):
            if a == 9:
                cpf_usuario += str(randint(0, 9))
            digito += int(cpf_usuario[i]) * cont_regr
            cont_regr -= 1
            if cont_regr == 1:
                digito *= 10
                digito %= 11
                digito = digito if digito <= 9 else 0
                cpf_usuario += str(digito)
                digito = 0
                if a == 10:
                    return cpf_usuario
                a = 10
                cont_regr = 11

cpf_gerado = cpf_retorna()

# print(f"CPF Gerado: {cpf_gerado}")
# print(validador(cpf_gerado))

for i in range(1, 101):
    print(i, cpf_retorna())