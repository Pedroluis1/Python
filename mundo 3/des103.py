def gols (jogador='<desconhecido>', gol=0):
    if jogador.strip() == '': 
        jogador = '<desconhecido>'
    if gol <= 0:
        gol = 0
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato.')


print('-'*30)
j = str(input('Nome do jogador: '))
g = int(input('Número de gols: '))
gols(j, g)
