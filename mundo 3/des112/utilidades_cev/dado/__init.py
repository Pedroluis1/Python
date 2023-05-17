def leiadinheiro(mensage):
    while True:
        number = str(input(mensage))
        if number.isnumeric():
            espaço = len(number)
            return float(number), espaço
        else:
            print(f"\033[31mERROR.'{number}' é um preço inválido!\033[m")
