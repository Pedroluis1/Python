valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite um último valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}º posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram ')
for n in valores:
    if n % 2 == 0:
        print(n,end=' ')
