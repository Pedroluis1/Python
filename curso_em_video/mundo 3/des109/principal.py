import moedas

p = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p)}')
print(f'Reduzindo 1%, temos {moedas.diminuir(p, 1, True)}')
print(f'Aumento 13%, temos {moedas.aumentar(p, 13, True)}')