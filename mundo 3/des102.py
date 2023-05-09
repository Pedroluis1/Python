def fatorial (num):
    """
    fatorial(n, show=False)
        -> calcula o fatorial de um número.
        :param n:
        :param show: (opcional) mostrar ou não a conta.
        :param return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range (num, 0, -1):
        f *= c
        return f


print(fatorial(5))