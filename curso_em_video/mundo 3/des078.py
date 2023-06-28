valores = []
for i in range(0, 5):
    valores.append(eval(input('Digite um valor para a lista: ')))
print(f'O valor maior é {max(valores)} e foi inserido nas posições', end='')
for i, v in enumerate(valores):
        if v == max(valores): print(f" {i+1}°... ",end='')
print(f'\nO valor menor é {min(valores)} e fica na {valores.index(min(valores))+1}° posiçao')

