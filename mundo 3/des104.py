def leiaint (mensage):
    while True:
        number = str(input(mensage))
        if number.isnumeric():
            print(f'You just entered the number {number}')
            return number
        else:
            print('\033[31mERROR. Enter a valid integer.\033[m')


n = leiaint('Digite um número: ')
