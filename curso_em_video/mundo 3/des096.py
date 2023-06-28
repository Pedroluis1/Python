def area (a, l):
    ar = l*a
    print(f'A área de um terreno {l} x {a} é de {ar}m².')


print('Controle de Terrenos')
print('-'*30)
la = float(input('LARGURA (m): '))
al = float(input('COMPRIMENTO (m): '))
area(l=la, a=al)