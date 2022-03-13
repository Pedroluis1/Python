aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*30)
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 4 < aluno['media'] <7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'-{k} é igual a {v}')