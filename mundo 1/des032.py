from datetime import date
ano = int(input('\033[33mQue ano quer analisar?\033[35m Coloque 0 para analisar o ano atual\033[m: '))
m = ano % 4, ano % 100 !=0 or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if m == 0:
    print(f'\033[35mO ano {ano} \033[32;1mÉ BISSEXTO\033[m')
else:
    print(f'\033[35mO ano {ano} \033[31;1mNÃO É BISSEXTO\033[m')
