print(20 * '\033[31m*\033[m', '\n\033[33mEMPRÉSTIMO BANCÁRIO\033[m')
print(20 * '\033[31m*\033[m')
casa = float(input('\033[33mValor desejado do emprétimo:\033[m \033[32mR$'))
salário = float(input('\033[33mSalário atual:\033[m \033[32mR$'))
pago = int(input('Será pago dividido em quantas parcelas? '))
if casa / pago > 0.3 * salário:
    print('\033[31mInfelizmente o empréstimo não poderá ser realizado.\033[m')
else:
    print(f'\033[32;4mEmpréstimo Bem Sucedido!!\033[m\n\033[33mO pagamento será realizado em '
          f'\033[4m{pago}\033[m \033[33mvezes de \033[4;32mR${casa / pago:.2f}\033[m\033[33m.')
enter = int(input('\033[33mAperte\033[32m 1\033[m \033[33mpara \033[32mconfirmar\033[33m o empréstimo.\n'
                  'Aperte\033[31m 2\033[33m para \033[31mcancelar\033[33m o empréstimo.\n'))
if enter == 1:
    print('\033[32;4mEmpréstimo \033[4mConfirmado!!\033[m')
elif enter == 2:
    print('\033[31mEmpréstimo \033[4mCancelado!\033[m')
else:
    print('\033[31;1mERROR!!!\033[m\n\033[31mDigite uma base de conversão válida!')
