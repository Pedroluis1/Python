from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6),
             'jogador 2': randint(1, 6),
             'jogador 3': randint(1, 6),
             'jogador 4': randint(1, 6)}
print('Valores sorteados:')
ranking = list()
for k, v in jogadores.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}° lugar---jogador {v[0]} com {v[1]}')