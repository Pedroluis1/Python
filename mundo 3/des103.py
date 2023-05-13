'''def gols (jogador='<desconhecido>', gol=0):
    if jogador.strip() == '': 
        jogador = '<desconhecido>'
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


print('-'*30)
j = str(input('Nome do jogador: '))
g = input('Número de gols: ')
if g.isnumeric():
    g =int(g)
else:
    g = 0
gols(j, g)'''

def ficha(n='', g=0):
    try:
        n = input('Nome do jogador: ')
        g = int(input('Número de gols: '))
    except ValueError:
        n = '<desconhecido>'
        g = 0
    print(f'O jogador {n} fez {g} gol(s).')


ficha()