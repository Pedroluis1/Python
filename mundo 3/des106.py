c = (
    '\033[m', # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - amarelo
    '\033[0;30;44m', # 4 - azul
    '\033[0;30;45m', # 5 - roxo
    '\033[7;30m' # 6 - branco
)
def escreva(p, cor=0):
    print(c[cor], end='')
    print('~'*(len(p)+4))
    print(f'  {p}  ')
    print('~'*(len(p)+4))
    print(c[0], end='')

def ajuda ():
    while True:
        escreva('Sistema de ajuda Pyhelp', 2)
        palavra = str(input('Função ou Biblioteca > ')).lower()
        if palavra == 'fim':
            escreva('Até logo', 1)
            return
        escreva(f'Acessando o manual do comando {palavra}', 4)
        print(c[6], end='')
        help(palavra)
        print(c[0], end='')

#Progama principal (no pycharm funciona direito)
ajuda()