def escreva(frase):
    print('--'*18)
    print(frase.center(36))
    print('--'*18)


def cores (cor, mensagem):
    c = (
        '\033[m', # 0 - sem cores
        '\033[31m', # 1 - vermelho
        '\033[32m', # 2 - verde
        '\033[33m', # 3 - amarelo
        '\033[34m', # 4 - azul
        '\033[35m', # 5 - roxo
        '\033[36m' # 6 - branco
    )
    print(c[cor], end='')
    print(mensagem,end='')
    print(c[0])

pessoas = {
    {'nome': 'ana','idade':44},
    {'nome':'pedro','idade':47},
    {'nome':'julia','idade':15},
    {'nome':'joao','idade':20}
}
'''def sistema(n):
    if n == 1:'''
print(pessoas)
for k, v in pessoas.items():
    print(f'{k} \t{v}')
