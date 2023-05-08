from time import sleep
def lista (*n):
    print('Analisando os valores passados...')
    sleep(0.5)
    for i in (n):
        print(f'{i} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(n)} ao todo.')
    sleep(0.5)
    print(f'O maior foi {max(n)}')
    sleep(0.5)
    print('-='*15)
    sleep(0.5)

# executar no Run without debugiggin para funcionar o sleep
print('-='*15) #Primeiro print
lista(7,5,4,1,2)
lista(90,20,3,1)
