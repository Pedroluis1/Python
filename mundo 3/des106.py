def escreva(p):
    print('~'*(len(p)+4))
    print(f'  {p}  ')
    print('~'*(len(p)+4))


def ajuda ():
    while True:
        escreva('Função de ajuda Pyhelp')
        palavra = str(input('Função ou Biblioteca > ')).lower()
        if palavra == 'fim':
            return
        escreva(f'Acessando o manual do comando {palavra}')
        help(palavra)


ajuda()