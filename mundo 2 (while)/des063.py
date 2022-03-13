print(20 * '-', '\nSEQUÊNCIA DE FIBOCCI')
print(20 * '-')
tm = int(input('quantos termos mostrar quer , que mostre ? '))
cont = 1
fibo = 0
while tm >= 0:
    print(fibo, end='→')
    fibo += cont
    cont = fibo - cont
    tm -= 1
print('Fim')
