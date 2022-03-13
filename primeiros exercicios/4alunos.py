from random import sample,choice,shuffle
'''alu1=input('Escreva o nome do aluno: ')
alu2=input('Escreva o nome do aluno: ')
alu3=input('Escreva o nome do aluno: ')
alu4=input('Escreva o nome do aluno: ')
print(f'O aluno sorteado foi: {random.sample((alu1,alu2,alu3,alu4),4)}')'''

alu1=input('\033[30mEscreva o nome do aluno: \033[m')
alu2=input('\033[31mEscreva o nome do aluno: \033[m')
alu3=input('\033[32mEscreva o nome do aluno: \033[m')
alu4=input('\033[34mEscreva o nome do aluno: \033[m')
print(f'Escolhido: {choice([alu1,alu2,alu3,alu4])}')
#[]= Lista necessário nesse caso

#Embaralhando de outra forma
alu1=input('\033[30mEscreva o nome do aluno: \033[m')
alu2=input('\033[31mEscreva o nome do aluno: \033[m')
alu3=input('\033[32mEscreva o nome do aluno: \033[m')
alu4=input('\033[34mEscreva o nome do aluno: \033[m')
lista=[alu1,alu2,alu3,alu4]
shuffle(lista)
print(f'\033[36mA ordem é:\033[30m {lista}')