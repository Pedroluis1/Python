print(f'{" COTROLE DE VENDAS ":-^40}')
tot = prm = bar = cont = 0
nombart = ''
while True:
    nom = str(input('Nome do produto: '))
    pr = float(input('Preço do produto:R$ '))
    qr = str(input('Continuar? S/N ')).strip().upper()
    while qr not in 'SN':
        qr = str(input('Continuar? S/N ')).strip().upper()
        if qr == 'N':
            break
    tot += pr
    cont += 1
    if cont == 1 or pr < bar:
        bar = pr
        nombart = nom
    if pr > 1000:
        prm += 1
    if qr == 'N':
        break
print(f'O total de gastos na compra foi de R${tot:.2f}.\n{prm} produtos custam acima de 1000 reais.\n'
      f'O nome do produto mais barato é {nombart}')
