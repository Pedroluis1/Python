times = 'ATHLETICO', 'ATLÉTICO-MG', 'GRÊMIO', 'ATLÉTICO-GO', 'SPORT', 'BAHIA', 'INTERNACIONAL', 'BRAGANTINO', \
        'BOTAFOGO', 'PALMEIRAS', 'SANTOS', 'CEARÁ', 'FLUMINENSE', 'SÃO PAULO', 'VASCO', 'CORINTHIANS', 'GOIÁS', 'CORITIBA', 'FORTALEZA', 'FLAMENGO'
print('\033[33mLista de times do brasileirão:\033[m ', end='')
for sel in times:
    print(f'\033[34m{sel}', end='\033[33m, ')
print('\nOs 5 primeiros são:',end=' ')
for sel in times[:5]:
    print(f'\033[32m{sel}',end='\033[33m, ')
print('\nOs 4 ultimos são:',end=' ')
for sel in times[-4:]:
    print(f'\033[31m{sel}',end='\033[33m, ')
print('\n\033[33mOs times em ordem alfabéticas:')
al = sorted(times)
for sel in al:
    print(f'\033[35m{sel}',end='\033[33m, ')
print(f'\nO \033[31mflamento\033[33m está na \033[31m{len(times)}°\033[33m posição')
print(f'O flamento está na {times.index("FLAMENGO")+1}° posição')
