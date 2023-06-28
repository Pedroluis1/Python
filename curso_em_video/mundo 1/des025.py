nome = str(input('\033[7;30;1mEscreva seu nome completo:\033[m ')).strip()
print(f'\033[7;30;1mSeu nome contém Silva:\033[m {"silva" in nome.lower()}')
