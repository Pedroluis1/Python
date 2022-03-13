from random import randint

comp = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram: ', end='')
for v in comp:
    print(v, end=' ')
print(f'\nO maior valor sorteado foi: {max(comp)}')
print(f'O menor valor sorteado foi: {min(comp)}')