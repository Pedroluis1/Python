from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('arquivo encontrado com sucesso')
else:
    print('arquivo não encontrado')
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        cabeçalho('op1')
    elif resposta == 2:
        cabeçalho('op2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO, por favor, Digite um número válido.\033[m')
        sleep(0.5)
