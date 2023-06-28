"""expr = str(input('Digite a expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida')
    #CONTÉM FALHA"""


expr = input('Digite sua expressão: ')
pilha = 0
for cont in expr:
    if cont == '(':
        pilha += 1
    if cont == ')':
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("sua expressão é válida!!")
else:
    print('Sua expressão é inválida!!')

