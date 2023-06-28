nono = int(input('Digite um número: '))
cont = contn = 0
while not nono == 101:
    cont += 1
    contn += nono
    nono = int(input('Digite um número: '))
print(f'Você digitou {cont} vezes.')
print(f'A soma dos números digitados é de {contn}')
