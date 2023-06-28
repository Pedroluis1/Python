print(20 * "\033[33;1m+", '\n\033[32mcálculadora de IMC')
print(20 * "\033[33;1m+\033[m")
high = float(input('\033[34mInforme sua altura: '))
peso = float(input('Informe seu peso: \033[m'))
imc = peso / (high * high)
if imc < 18.5:
    print(f'\033[35;1mAbaixo do peso.\nCom o imc de \033[34m{imc:.2f}\033[m')
elif imc < 25:
    print(f'\033[32;1mPeso ideal.\nCom o imc de \033[34m{imc:.2f}\033[m')
elif imc < 30:
    print(f'\033[33;1mSobrepeso.\nCom o imc de \033[34m{imc:.2f}\033[m')
elif imc < 40:
    print(f'\033[31mObesidade.\nCom o imc de \033[34m{imc:.2f}\033[m')
else:
    print(f'\033[31;1mObesidade mórbida.\nCom o imc de \033[34m{imc:.2f}\033[m')
