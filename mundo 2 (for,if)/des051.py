print(20 * '=', '\nTERMOS DE UMA PA')
print(20 * '=')
termo = int(input('Primeiro termo: '))
razao = int(input('razão: '))
for pa in range(termo, termo + razao * 8, razao):
    print(pa, end=' → ')
print('END.')
