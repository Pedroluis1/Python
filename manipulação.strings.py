# fatiamento
frase = 'você é amazing e incrivel'
print(f'A frase é: \n{frase}\n')
print(frase[7:14])
print(frase[7:25:2])
print(frase[:14])
print(frase[7:])
print(frase[7::4])
# análise
print(f'A frase é constituida de {len(frase)} caracteres')
print(f'A frase contém {frase.count("a")} a')
print(frase.count('o',7,14))
print('incrivel'in frase)
palavra = input('digite a letra ou a palavra que queira encontrar:')
print(f'A palavra/letra {palavra}, está localizada no carater {frase.find(palavra)}')
print(f'A palavra "você" está localizado no caracter {frase.find("você")}\n')
# trasnformaçâo
print(frase.replace('incrivel','um Boxta'))# Não é a original, é como se fosse uma cópia
print(frase.upper())
print(frase.lower())
print(frase.capitalize())# primeira letra "V"
print(frase.title())
otro ='         Eae parceiro         '
print(otro.strip())
print(otro.rstrip())# Direita
print(otro.lstrip(),end=2*'\n')# Esquerda
# Divisão
print(frase.split(' '.join(frase)))
print('-'.join(frase))
print('\n-'.join(frase))