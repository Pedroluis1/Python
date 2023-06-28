cadastro = []
temp = []
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('nota 1: ')))
    temp.append(float(input('nota 2: ')))
    cadastro.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? N/S '))
    if resp in 'Nn':
        break
print('-='*30,'\n',f'{"NOME":>10}{"MÉDIA":>17}','\n','-'*34)

for i in range (0, len(cadastro)):
    print(i,f'{cadastro[i][0]:>10}',f'{(cadastro[i][1]+cadastro[i][2])/2:>14.1f}')
print('-'*34)
while True:
    res = int(input('Mostrar as notas de qual aluno? (999 interrompe):'))
    if res == 999:
        print('Finalizado!')
        break
    elif res > len(cadastro)-1:
        print('\n',' Número não encontrado digite novamente: (999 interrompe) ', '\n')
    else:
        print('\n',f' As notas de {cadastro[res][0].upper()} são, Nota1 "{cadastro [res][1]}", Nota2 "{cadastro[res][2]}".','\n')


