palavra = str(input('\033[34;1mEscreva uma frase\033[m: ')).strip()# or lower.
print(f"\033[30mLetra\033[m \033[31m'a'\033[m \033[30mapareceu\033[m \033[31m{(palavra.lower().count('a'))}"
      f"\033[m \033[30mvezes.\033[m")
print(f'\033[30mA posição da letra \033[31m"a"\033[30m aparece pela primeira vez, na posição\033[m \033[31m'
      f'{palavra.lower().find("a")+1}\033[m \033[30me\033[m',end=' ')
print(f'\033[30maparece pela última vez, na posição\033[m \033[31m{palavra.lower().rfind("a")+1}\033[m')
