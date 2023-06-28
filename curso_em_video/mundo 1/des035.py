print(20 * '\033[33m-=\033[m', '\n\033[1;31mAnalisador de triângulos\033[m')
print(20 * '\033[33m-=\033[m')
pr = float(input('\033[;36;1mPrimeiro segmento: '))
pr2 = float(input('Segundo seguemento: '))
pr3 = float(input('Terceiro segmento: \033[m'))
todos = pr, pr2, pr3
if max(todos) < pr + pr2 + pr3 - max(todos):
    print('Os segmentos acima \033[32;1mPODEM FORMAR\033[m um trângulo!')
else:
    print('Os segmentos acima \033[31;1mNÃO PODEM FORMAR\033[m um triângulo!')

"""De outra forma:
if pr < pr2 + pr3 and pr2 + pr + pr3 and pr3 + pr2 + pr:"""