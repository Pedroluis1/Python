def voto (idade):
    from datetime import date
    idade = date.today().year - idade
    if 16 >= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
        

print('-'*30)
i = int(input('Em que ano você nasceu? '))
print(voto(i))