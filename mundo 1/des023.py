# modo string
"""num = str(input('Digite um número de 4 digitos: ')[:9999])
print(f'unidade: {num[3]}\ndezena: {num[2]}\ncentena: {num[1]}\nmilhar: {num[0]}')"""  # contém falhas!!
# matemático (melhor)
num = int(input("\033[36mDigite um número entre 0 e 9999:\033[m "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'\033[30munidade: {u}\033[31m\ndezena: {d}\033[32m\ncentena: {c}\033[33m\nmilhar: {m}')
