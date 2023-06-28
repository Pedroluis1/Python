def metade (num):
    return num/2


def dobro (num):
    return num*2


def aumentar (num, c=0):
    return ((c/100)*num)+num


def diminuir (num, c=0):
    return num - ((c/100)*num)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:<.2f}'.replace('.', ',')