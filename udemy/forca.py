import os

palavra_secreta = 'perfume'
letras_acertadas = ''

while True:
    letra_digitada = input('Digite uma letra: ')
    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('Você venceu, parabéns!')
    print({palavra_formada})


# Melhorias:
# - Número de tentativas
# - fazer o usuário escolher a palavra e o tópico (limpar depois disso)
# - número de tentativvas limitada
# - mostrar os espaços se a paalavra tiver espaços