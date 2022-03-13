# primeira forma
"""from math import factorial
n = int(input('Digite o valor que deseja fatorar: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')"""

# Segunda forma com while
"""n = int(input('Digite o valor que deseja fatorar: '))
c = n
rial = 1
print(f'Calculando, {n}! ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    rial *= c
    c -=1
print(rial)"""
# Terceira forma com For
n = int(input('Digite o valor que deseja fatorar: '))
c = n
f = 1
for p in range(n, 0, -1):
    f *= p
    p -= 1
print(f'O fatorial de {n} é {f}')
