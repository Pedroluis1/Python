from time import sleep
def lista (*n):
    print('Analisando os valores passados...', flush=True)
    sleep(0.5)
    for i in (n):
        print(f'{i} ', end='',flush=True)
        sleep(0.5)
    print(f'Foram informados {len(n)} ao todo.', flush=True)
    sleep(0.5)
    print(f'O maior foi {max(n)}', flush=True)
    sleep(0.5)
    print('-='*15, flush=True)
    sleep(0.5)

# executar no Run without debugiggin para funcionar o sleep
print('-='*15, flush=True) #Primeiro print
lista(7,5,4,1,2)
lista(90,20,3,1)
