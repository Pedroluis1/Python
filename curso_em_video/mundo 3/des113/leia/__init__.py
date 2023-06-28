def leiaint (mensage):
    import cor
    while True:
        try:
            number = int(input(mensage))
        except (ValueError, TypeError):
            print(f"\033[31mERROR. Digite um número inteiro!\033[m")
            continue
        except KeyboardInterrupt:
            cor.cores(3, 'O usuário preferiu não digitar nada.')
            return 'nenhum'
        else:
            return number


def leiafloat(mensage):
    import cor
    while True:
        try:
            n = float((input(mensage)))
        except(TypeError, ValueError):
            cor.cores(1, 'Número inválido, digite um número real.')
            continue
        except KeyboardInterrupt:
            cor.cores(3, 'O usuário preferiu não digitar nada.')
            return 'nenhum'
        else:
            return float(n)
        
