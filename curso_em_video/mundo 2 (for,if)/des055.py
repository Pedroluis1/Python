its = []
for re in range(1, 6):
    peso = float(input(f'peso da {re}º pessoa: '))
    its += [peso]
print(f'maior peso lido {max(its)}kilos.')
print(f'menor peso lido {min(its)}kilos.')
