contmen = contwoman = eith = 0
while True:
    ida = int(input('informe sua idade: '))
    s = str(input('Infrome seu sexo M/F: '))
    while s not in 'MmFf':
        s = str(input('Infrome seu sexo M/F: '))
        if s in 'Mm':
            contmen += 1
        if ida <= 18:
            eith += 1
        if s in 'Ff' and ida < 21:
            contwoman += 1
    pe = str(input('Quer continuar S/N? '))
    if pe in 'Nn':
        break
    while pe not in ' SsNn':
        pi = str(input('Quer continuar S/N? ')).strip().upper()
        if pi == 'N':
            break
    if pi == 'N':
        break
print(f'\nNo grupo:\ncontém {contmen} homens.\ncontém {eith} pessoas menores de 18 anos.'
      f'\ncontém {contwoman} mulheres com menos de 21 anos.')
