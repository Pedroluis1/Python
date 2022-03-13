from emoji import emojize
print('Saiba quanto ganha com um dia de trabalho.')
print(emojize(':arrow_double_down:'*15,use_aliases=True))
s = float(input('salário:R$'))
d = int(input('Quantos dias da semana você trabalha: '))
print(f'Um dia de trabalho seu vale aproximadamente {(s / 4) / d:.2f} reais, e uma semana {s / 4} reais.')
