print(20 * '\033[33m=\033[m', '\n\033[34m10 TERMOS DE UMA PA\033[m')
print(20 * '\033[33m=\033[m')
termo = int(input('Primeiro termo: '))
razao = int(input('razão: '))
primeiro = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro}', end=' → ')
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('\033[34mQuer mostrar quantos termos a mais?\033[m '))
print(f'Progressão finalizada com {total} termos mostrados.')

