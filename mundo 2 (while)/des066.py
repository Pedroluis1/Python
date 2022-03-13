'''cont = som = 0
while True:
    lu = int(input('Digite um valor (999 para parar): '))
    if lu == 999:
        break
    cont += 1
    som += lu
print(f'A soma dos {cont} valores, foi {som}.')'''

s = q = n = 0
while n != 999:
    s += n
    q += 1
    n = int(input('Digite um número [999 PARA PARAR]: '))
print(f'A soma dos {q} números foi {s}!')
