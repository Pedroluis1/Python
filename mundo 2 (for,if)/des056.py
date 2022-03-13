media = 0
maioridadedehomem = 0
nomevelho = ''
totomulher20 = 0
for p in range(1, 5):
    print(7 * '-', f'{p}º pessoa', 7 * '-')
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo M/F : ')).strip().upper()
    media += idade / 4  # media da idade do grupo
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'fF' and idade < 20:
        totomulher20 += 1
print(f'A média de idade do grupo é de {media:.0f} anos.')
print(f'O homem mais velho do grupo e o {nomevelho} com {maioridadedehomem} anos.')
print(f'Ao todo são {totomulher20} mulheres com menos de 20 anos.')
