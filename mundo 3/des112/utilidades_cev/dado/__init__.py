def leiadinheiro(mensage):
    while True:
        number = str(input(mensage)).replace(',', '.').strip()
        if number.isalpha() or number == '':
            # isalpha nessa situação é melhor que isnumerc, (por conta de ler o ponto)
            print(f"\033[31mERROR.'{number}' é um preço inválido!\033[m")
        else:
            return float(number)