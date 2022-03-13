print('ALUGUEL DE CARRO\n ')
i=int(input('Quantos dias alugados? '))
k=float(input('Quantos Km rodados? '))
print(f'\nDias: R${i*60}\nKm: {k*0.15:.2f}\nSendo o total a pagar de: R${i*60+k*0.15}')