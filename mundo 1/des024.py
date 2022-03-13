cid = input('\033[31;1mDigite o nome de sua cidade:\033[m ').strip()
print(f'\033[34;1mO nome da sua cidade começa com o nome santo:\033[31m {cid[:5].upper() == "SANTO"}')
