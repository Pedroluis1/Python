def contagem(i, f, p):
    if p == 0:
        p = 1
    if i and f > 0 > p:
        p = p + (2*(-p)) # 40 50 -1 ( convertendo para o positivo)
        print(p)
    print(f'\nContagem de {i} até {f-1} de {p} em {p}')
    if i > f:
        p = -p #50 10 (convertendo para o negativo)
        f = f -2
        print(p,'if')
    if f<0:
        p = -p # (convertendo para o negativo) fim: -10

#?? converter (adapitando) quando 90 -40 10 e vice versa!! 



    for c in range (i, f, p):
        print( f'{c} ', end='')
    print('FIM ')
    print('-='*20)

        

print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))+1
passo = int(input('Passo: '))
contagem(inicio, fim, passo)