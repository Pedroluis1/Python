def metade (preço=0):
    res = preço/2
    return f'R${res:<.2f}'.replace('.', ',')


def dobro (preço=0):
    res = preço*2
    return f'R${res:<.2f}'.replace('.', ',')


def aumentar (preço=0, c=0, format=False):
    res = ((c/100)*preço)+preço
    return res if not format else moeda(preço)


def diminuir (preço=0, c=0, format=False):
    res = preço - ((c/100)*preço)
    return res if format is False else moeda(preço)


def moeda(preço=0, moeda='R$'):
    return f'R${preço:<.2f}'.replace('.', ',')
