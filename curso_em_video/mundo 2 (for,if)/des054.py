from datetime import date

cont = 0
cont2 = 0
for nas in range(1, 8):
    nasc = int(input(f'Em que ano a {nas}º pessoa nasceu? '))
    idade = date.today().year - nasc
    if idade >= 21:
        cont += 1
    else:
        cont2 += 1
if cont == 1:
    print(f'Ao todo tivemos {cont} pessoa com maior idade (21 anos).')
elif cont == 0:
    print('Ao todo tivemos nenhuma pessoa com maior idade (21anos).')
else:
    print(f'Ao todo tivemos {cont} pessoas com maior idade (21anos).')
if cont2 == 1:
    print(f'E {cont2} pessoa com menos de 21 anos.')
elif cont2 == 0:
    print('E nenhuma pessoa com menos de 21 anos.')
else:
    print(f'E {cont2} pessoas com menor idade, de 21 anos.')
