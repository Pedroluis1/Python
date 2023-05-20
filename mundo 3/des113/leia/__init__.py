def leiaint (mensage):
    try:
        number = int(input(mensage))
    except (ValueError, TypeError):
        print(f"\033[31mERROR. Digite um número inteiro!\033[m")
        continue
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar nada.')
    else:
        print(f'{number} é um número válido.')


