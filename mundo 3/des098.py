from time import sleep
def contagem(i, f, p):
    if p == 0:
        p = 1
    if i and f > 0 > p:
        p = p + (2*(-p)) # 40 50 -1 ( convertendo para o positivo)
    print(f'Contagem de {i} até {f-1} de {p} em {p}', flush=True)
    sleep(1)
    if i > f:
        p = -p #50 10 (convertendo para o negativo)
        f = f -2
    if f<0:
        p = -p # (convertendo para o negativo) fim: -10
    if i > 0 > f:
        p = -p #?? converter (adapitando) quando 90 -40 10 e vice versa!! 
    for c in range (i, f, p):
        print( f'{c} ', end='', flush=True)# flush=True
        sleep(0.4)
    print('FIM! ')

    print('-='*20)


print('-='*20)
contagem(1, 11, 1)
contagem(10, 1, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))+1
passo = int(input('Passo: '))
print('-='*20)
contagem(inicio, fim, passo)