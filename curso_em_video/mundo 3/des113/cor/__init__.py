def cores (cor, mensagem):
    c = (
        '\033[m', # 0 - sem cores
        '\033[31m', # 1 - vermelho
        '\033[32m', # 2 - verde
        '\033[33m', # 3 - amarelo
        '\033[34m', # 4 - azul
        '\033[35m', # 5 - roxo
        '\033[36m' # 6 - branco
    )
    print(c[cor], end='')
    print(mensagem,end='')
    print(c[0])