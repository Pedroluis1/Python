pr = str(input('\033[32;1mEscreva seu nome completo\033[m: ')).strip()
print(f'\033[32;1mSeu primeiro nome é\033[m {pr.title().split()[0]}')
print(f'\033[32;1mSeu último nome é\033[m {pr.split()[len(pr.split())-1]}')
