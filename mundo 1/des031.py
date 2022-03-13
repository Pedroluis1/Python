
dis = float(input("\033[34mQual vai ser a distância da sua viagem em km?\033[m "))
if dis <= 200:
    print(f'\033[36mo preço da passagem custará \033[33;4mR${dis*0.50}\033[m')
else:
    print(f'\033[36mo preço da passagem custará \033[33;4mR${dis*0.45}\033[m')
if dis < 50:
    print('\033[33;1mIIIIIHHHHH\033[31m ala vai viajar para a quadra do lado?\033[m \033[33mkkkkkk\033[m'
          ,8*'\n','\033[30mobs:\033[35mpiadinha sem graça\033[m')
