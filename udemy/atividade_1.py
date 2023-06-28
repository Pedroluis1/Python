print('Jogo da Forca')
print('-'*20)
palavra = 'apple'

# while True:
#     print('Palavra Secreta: ',end='')
#     for letra in palavra:
#         print('*',end='')
#     entrada = str(input('\nDigite uma letra: ')).strip()
#     if len(entrada) > 1: #validação de só uma entrada
#         print('Digite apenas uma letra.')
#         continue


#     if entrada in palavra:#validação das letra na frase
#         print(palavra.find(entrada))
#         print(palavra[palavra.find(entrada)])

entrada = 'p'
print(palavra.find(entrada))
