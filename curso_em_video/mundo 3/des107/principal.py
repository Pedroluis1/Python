import moedas

p = float(input('Digite o preço: '))
print(f'A metade do {p} é {moedas.metade(p)}')
print(f'O dobro do {p} é {moedas.dobro(p)}')
print(f'Reduzindo 1%, tmeos {moedas.diminuir(p, 1)}')
print(f'Aumento 13%, temos {moedas.aumentar(p, 13)}')