from datetime import date
def voto (idade):
    idade = date.today().year - idade
    if idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    elif idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'Com {idade} anos: NÃO VOTA.')
        

print('-'*27)
i = int(input('EM que ano você nasceu? '))
voto(i)