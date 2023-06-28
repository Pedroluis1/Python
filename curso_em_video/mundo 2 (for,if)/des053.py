frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
'''inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(junto, inverso)
if junto == inverso:
    print('temos um palíndromo!')
else:
    print('não temos um palíndromo!')
