from lib.interface import *
from lib.arquivo import *
from time import sleep


arq = 'mundo 3/115 treino/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        #opção de listar o conteúdo do arquivo!
        sleep(0.5)
        lerArquivo(arq)
        sleep(0.5)
    elif resposta == 2:
        #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(0.5)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mERRO, por favor, Digite um número válido.\033[m')
        sleep(0.5)
