def fatorial(num, show=False):
    """
    fatorial(n, show=False)
        -> calcula o fatorial de um número.
        :param n:
        :param show: (opcional) mostrar ou não a conta.
        :param return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#programa principal
print(fatorial(5, show=True))
#help(fatorial)
