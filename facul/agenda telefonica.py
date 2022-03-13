agenda = dict()
td = list()
nomes = list()
cont = 0
print('     AGENDA TELEFONICA    ')
while True:
    menu = int(input('[0] Mostrar agenda\n'
                     '[1] Novo contato\n'
                     '[2] Pesquisar contato\n'
                     '[3] Remover ou fazer alteração do contato\n:'))
    while menu not in (0, 1, 2, 3):
        print('----Digite um número válido----')
        menu = int(input(f'[1] Novo contato\n'
                         f'[2] Pesquisar contato\n'
                         f'[3] Remover ou fazer alteração do contato\n:'))
    if menu == 0:
        print('  ', end='')
        for k, v in agenda.items():
            print(f'{k}', 17 * ' ', end='')
        print()
        for k, v in enumerate(td):
            if cont != len(td) + 1:
                print(f'{k} {td[cont]["nome"]:<22}'
                      f'{td[cont]["telefone"]:<26}'
                      f'{td[cont]["email"]:<23}'
                      f'{td[cont]["twitter"]:<25}'
                      f'{td[cont]["instagram"]:<5}')
                cont += 1
        cont = 0
        print()
    # MENU==1
    elif menu == 1:
        agenda['nome'] = input(str('Nome: ')).lower()
        try:
            agenda['telefone'] = int(input('Telefone: '))
        except:
            print('\033[31mDigite somente números!!!\033[m')
            agenda['telefone'] = int(input('Telefone: '))
        agenda['email'] = input('Email: ')
        agenda['twitter'] = input('twitter: ')
        agenda['instagram'] = input('Instagram: ')
        td.append(agenda.copy())
        nomes.append(agenda.copy()['nome'])
        print(f'Contato "{agenda["nome"]}" adicionado na agenda!')
        print(menu)
    # MENU==2
    elif menu == 2:
        try:
            pesquisar = input(f'Pesquisar nome: ')
            num = (nomes.index(pesquisar.lower()))
            print(f'{num} - {td[num]}')
        except:
            print('O item não foi encontrado.')
        print()
    # MENU==3
    elif menu == 3:
        opcao = int(input('[1] Remover contato\n[2] Fazer alteração\n:'))
        while opcao not in (1, 2):
            print('----Digite um número válido----')
            print(opcao)
        # OPCAO=1
        if opcao == 1:
            try:
                remcont = input('Nome do contato que deseja remover: ').lower()
                num2 = (nomes.index(remcont.lower()))
                td.pop(num2)
                print(f'Contato {remcont} excluido')
            except:
                print('O item não foi encontrado.')
        elif opcao == 2:
            try:
                altcont = input('Nome do contato que deseja fazer alteração: ').lower()
                num2 = (nomes.index(altcont.lower()))
                qual = int(input('Em qual setor deseja fazer alteração:\n'
                                 '[1] Nome\n[2] Telefone\n[3] Email\n[4] Twitter\n[5] Instagram\n:'))
                while qual not in (1, 2, 3, 4, 5):
                    print('----Digite um número válido----')
                    print(qual)
                if qual == 1:
                    novnom = input('Novo nome do contato: ')
                    td[num2] = {**td[num2], 'nome': novnom}
                    print(f'contato alterado!\n{td[num2]}')
                elif qual == 2:
                    novtel = input('Novo telefone do contato: ')
                    td[num2] = {**td[num2], 'telefone': novtel}
                    print(f'contato alterado!\n{td[num2]}')
                elif qual == 3:
                    novema = input('Novo email do contato: ')
                    td[num2] = {**td[num2], 'email': novema}
                    print(f'contato alterado!\n{td[num2]}')
                elif qual == 4:
                    novtwi = input('Novo twitter do contato: ')
                    td[num2] = {**td[num2], 'twitter': novtwi}
                    print(f'contato alterado!\n{td[num2]}')
                elif qual == 5:
                    novinsta = input("Novo instagram do contato: ")
                    td[num2] = {**td[num2], 'instagram': novinsta}
                    print(f'contato alterado!\n{td[num2]}')
            except:
                print('O item não foi encontrado.')
