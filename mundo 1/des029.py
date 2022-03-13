velo = float(input('velocidade do carro: '))
multa=(velo-80)*7
if velo > 80:
    print(f'\033[31;1mMULTADO!!\033[m \033[31mvocê excedeu o limite permitido que é de 80km/h'
          f'\nVocê deve pagar uma multa de\033[m \033[33mR${multa:.2f}!')
    print('\033[32mTenha um Bom Dia! Dirija com segurança!\033[m')
else:
    print('\033[32mTenha um Bom Dia! Dirija com segurança!\033[m')
