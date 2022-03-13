num = []
while True:
    num.append(int(input('Digite um numero: ')))
    cont = str(input('Quer continuar? s/n ')).upper().strip()
    if cont == 'N':
        break
num.sort(reverse=True)
print(f'O total de número digitados foram {len(num)}')
print(f'A lista em forma decrescente: {num}')
if 5 in num:
    print(f'A lista contém o número 5.')
else:
    print('A lista não contém o número 5.')
