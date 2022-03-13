valores = []
for i in range(0, 5):
    valores.append(eval(input('Digite um valor para a lista: ')))
print(f'O valor maior é {max(valores)} e fica na {valores.index(max(valores))+1}° posiçao')
print(f'O valor menor é {min(valores)} e fica na {valores.index(min(valores))+1}° posiçao')
