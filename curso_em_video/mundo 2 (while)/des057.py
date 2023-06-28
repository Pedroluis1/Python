s = str(input('Informe seu sexo F/M: ')).upper().strip()[0]
while s not in 'MF':
    s = str(input('Dados inválidos.Informe seu sexo F/M: ')).upper().strip()[0]
print(f'sexo {s} registrado com sucesso! ')
