import moedas

p = float(input('Digite o preço: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Reduzindo 1%, temos {moedas.moeda(moedas.diminuir(p, 1))}')
print(f'Aumento 13%, temos {moedas.moeda(moedas.aumentar(p, 13))}')