from random import randint
from time import sleep

def genum ():
    print('Sorteando 5 valores da lista: ',end='', flush=True)
    for i in range (0, 6):
        nume = randint(1, 9)
        lista.append(nume)
        print(f'{nume} ',end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somando (l):
    p = 0
    for v in l:
        if v % 2 == 0:
            p += v
    print(f'Somando os valores pares de {lista}, temos {p}')


lista = list()
genum()
somando(lista)
