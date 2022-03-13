from datetime import date

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['idade'] = (date.today().year - int(input('Ano de nascimento: ')))
cadastro['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['Carteira'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposentadoria'] = 65 - (date.today().year - cadastro['contratação'])
print(30 * '-=')
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor de {v}')
