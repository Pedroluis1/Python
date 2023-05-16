def aumentar (num):
    print(f'A metade de {num} é {num/2}')


def dobro (num):
    print(f' O dobro de {num} é {num*2}')


def diminuir (num, c=10):
    print(f'Aumentando {c}, temos {((c/100)*num)+num}')


def metade (num, c=10):
    return ((c/100)*num)-num
