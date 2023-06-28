valores = [[], []]
val = 0
for c in range(1, 8):
    val = int(input(f'Digite o {c}° valor: '))
    if val % 2 == 0:
        valores[0].append(val)
    else:
        valores[1].append(val)
valores[0].sort()
valores[1].sort()
print(f'valores impares: {valores[1]}')
print(f'valores pares: {valores[0]}')
