from datetime import date
def voto (ano):
    print(f'Com {date.today().year - ano} anos: ', end='')
    if date.today().year - ano > 18:
        print('VOTO OBRIGATÓRIO.')
    elif date.today().year - ano < 18:
        print('NÃO VOTA.')
    else:
        print('VOTO OPCIONAL.')


ano = int(input(30*'-','\nEm que ano você nasceu? '))
voto(ano)