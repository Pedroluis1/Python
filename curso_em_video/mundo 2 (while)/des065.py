cont = soma = 0
maior = []
while True:
    nono = int(input('Enter a value: '))
    sp = str(input('want carry on, Y / N? '))
    cont += 1
    soma += nono
    maior += [nono]
    if sp in 'Nn':
        break
print(f'A média de todos os válores digitados é {soma / cont:.1f}')
print(f'A soma de todos os válores digitados é de {soma}')
print(f'O maior número digitado foi {max(maior)}')
print(f'O menor número digitado foi {min(maior)}')
