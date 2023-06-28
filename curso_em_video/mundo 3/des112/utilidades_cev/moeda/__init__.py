def metade(preço=0):
    res = preço / 2
    return moeda(res)


def dobro(preço=0):
    res = preço * 2
    return moeda(res)


def aumentar(preço=0, c=0, format=False):
    res = ((c / 100) * preço) + preço
    return res if not format else moeda(res)


def diminuir(preço=0, c=0, format=False):
    res = preço - ((c / 100) * preço)
    return res if format is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'R${preço:<8.2f}'.replace('.', ',')


def resumo(preço=0, aumento=10, redução=5):
    """
    resumo (preço, aumento=10, redução=5)
        -> calcula a metade, o dobro, aumento e dimnuição em porcentagem de um preço.
        :param preço: preço do produto.
        :param aumento: aumento em porcentagem.
        :param resução: resução em porcentagem.
        :param print: formatado.
    """
    print('-' * 35)
    print('Resumo do valor'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-' * 35)
