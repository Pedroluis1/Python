print(20 * '\033[33m-=\033[m', '\n\033[1;31mAnalisador de triângulos\033[m')
print(20 * '\033[33m-=\033[m')
ps = float(input('\033[36mPrimeiro Segmento: \033[m'))
ss = float(input('\033[36mSegundo Segmento: \033[m'))
ts = float(input('\033[36mTerceiro Segmento: \033[m'))
todos = ps, ss, ts
if max(todos) < ps + ss + ts - max(todos):
    print('\033[30mOs segmentos acima \033[32;1mPODEM FORMAR\033[m \033[30mum trângulo!\033[m')
    if ps == ss == ts:
        print('\033[33;1mO triângulo é Equilátero.\033[m')
    elif ps == ss != ts or ss == ts != ps or ts == ps != ss:
        print('\033[33;1mO triângulo é Isóceles.\033[m')
    elif ps != ss != ts:
        print('\033[33;1mO triângulo é Escaleno.\033[m')
else:
    print('\033[36mOs segmentos acima \033[31;1mNÃO PODEM FORMAR\033[36m um triângulo!\033[m')
