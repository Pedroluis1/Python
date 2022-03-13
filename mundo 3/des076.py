materiais = ('Lápis', 1.75,
             'Borracha', 2,
             'Caderno', 4.20,
             'Estojo', 25,
             'Transferidor', 4.20,
             'Compasso', 9.99,
             'Mochila', 120.50,
             'Canetas', 22.30)
print('-'*35,'\nLISTAGEM DE PREÇOS')
print('-'*35)
for pos in range(0,len(materiais)):
    if pos % 2 == 0:
        print(f'{materiais[pos]:.<25}',end='')
    else:
        print(f'R${materiais[pos]:>5.2f}')
