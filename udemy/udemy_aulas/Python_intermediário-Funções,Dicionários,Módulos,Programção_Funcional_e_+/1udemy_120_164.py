#letras maiusculas em variáveis sãi usadas para demonstrar que é uma \
#variável imutável, valor fixo (para não mudar)

# ... (caso  a váriavel ou o código precisa terminar)

# Ctrl Shift L ou f2, (para mudar todas as instâncias de uma variável)

variavel1 = 'ahhh'
variavel2 = 'ahhh'
print(id(variavel2)) 
print(id(variavel1)) # Compartilham o mesmo id por terem o mesmo valor  

#Vê se existe com poder de adicionar se não existir:
print(pessoa.get('sobrenome', Nome))

#Outro exemplo (setdefault):
pessoa = {
    'nome': 'Luiz otavio',
    'sobrenome': 'Miranda',
    'idade': 900,
    }

pessoa.setdefault('idade', 0) #se não estiver idade a idade será 0, senão ignora
print(pessoa['idade'])

#shallow copy e deep copy, (cópia rasa, cópia profunda): .copy(), .deepcopy()
# Em Ordenar.py, em outros!
'''Diferença de .pop() e delete, .pop() retorna o valor a ser excluído antes de excluir
.popitem(), para excluir itens de um dicionario.
.update({}), pode criar chaves e atualizar as existentes, pode também passar argumentos nomeados.
	Exemplo:	p1.update(nome='novovalor', idade= 30)'''

#Utilizando o update em forma de tupla () ou lista []:
tupla = (('nome', 'novo valor'), ('idade', 30))
p1.update(tupla)

#Sets são eficientes para remover valores duplicados, Não garantem ordem!!!, somente valores imutáveis, não tem indice
# set = {1,2,3} or set()
# set.add('luiz')
# dicio = {}
l1 = [1,2,3,3,3,3,3,1]
s1 = set(l1)
l2 = list(s1)
print(l2)

# exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra)
    print(letras)

# Desempacotamento de dicionários
pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza'
}
(a1,a2), (b1,b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoas_completa = {**pessoa, **dados_pessoa}

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(nome='Joana', qlq='123')
mostro_argumentos_nomeados(**pessoas_completa)

# Aula 136, 137 List comprehension
print(list(range(10)))

lista = [numero for numero in range(10)]
'''lisrta = [
    numero * 2 #mapeamento (pegando um indice pro outro)
    for numero in range(10)
]'''
print(lista)

# mapeamento de dados em list comprehension
produtos = [
    {'nome':'p1', 'preco':20,},
    {'nome':'p2', 'preco':10,},
    {'nome':'p3', 'preco':20,},
]
novos_produtos = [
    produtos['nome']
    for produto in produtos
]

# atualizando os dados do dicionário
'''novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5} # Aumento de 5% de cada produto
    for produto in produtos
]'''

#adicionando condições
'''novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos'''

#adicionando filtro
'''novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.5}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10''' # adicionado filtro

print(novos_produtos)
print(*novos_produtos, sep='\n')

# Aula 138 filtro de dados em list comprehension (filter) pprint (formatação do comando de saida)
# import pprint
# pprint.pprint(novos_produtos, sort_dicts=False, width=40)

# Filtro (não contém else)
lista_138 = [n for n in range(10) if n < 5]
print(lista_138)

# Aula 139 list comprehension com mais de um for

lista_139 = []
for x in range(3):
    for y in range(3):
        lista_139.append((x,y)) # tupla para mapeamento

# com list comprehension
lista_139 = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista_139)

# Aula 141 Dictionary comprehension e Set comprehension
produto_141 = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc_141 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor  # checando com o isinstance, se eu quiser dois valores na isinstance 'str' posso usar a tupla "(str, int)"
    for chave, valor
    in produtos.items()
    if chave != 'categoria' # Filtro
}

# Aula 142 isinstance - para saber se o objeto é determinado tipo
lista_142 = [
    'a', 1, 1.1, true, [0, 1, 2], (1, 2), {1, 2}, {'nome': 'luiz'}
]

for item in lista_142:
    if isinstance(item, set):
        print(item, isinstance(item, set))

# Aula 143 
# Valores Truthy e Falsy, tipos Mutáveis e imutáveis
# mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)

# Aula 144 dir, hasattr e getattr em python
#dir(string) no terminal, conferir se o método so objeto está lá

string_144 = 'luiz'
metodo = 'upper'

if hasattr(string,'upper'):
    print('Existe upper')
    print(string_144.upper())

# com gettr

if hasattr(string,'upper'):
    print('Existe upper')
    print(getattr(string_144, metodo)())

# Aula 145 Generator expression, Iterables e Iterators em Python
iterable = ['EU', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Aula 146 Generator expression, Iterables e Iterators em Python
iterable = ['EU', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(1000)]
generator = (n for n in range(1000)) # Função pausada
print(generator)

import sys
print(sys.getsizeof(lista)) # tamanho da lista em bits
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

'''for n in generator:
    print(n)''' # mostrando todos os itens no generator

# Aula 147 Introdução às Generator functions em Python
def generator_147(n=0):
    yield 1 # Pausa (Toda função que contém o yield é uma generator function)
    print('Continuando...')
    yield 2 # Pausar
    print('mais uma...')
    yield 3
    print('Vou terminar')
    return 'ACABOU'

gen_147 = generator_147(n=0)
print(gen_147)
print(next(gen_147))

for n in gen_147:
    print(n)
# testar as pausas do yield no while (entender mais)

# Aula 148 yiels from em generetor functions
# Yield from
def gen1_148():
    yield 1 
    yield 2
    yield 3

def gen2_148():
    yield from gen1_148() #continuação do gen1_148
    yield 4
    yield 5
    yield 6

g_148 = gen2_148()
for numero in g_148:
    print(numero)
 
 # OU
 '''def gen2_148(gen):
    yield from gen
    yield 4
    yield 5
    yield 6'''

# Aula 152 raise - lançando exceções (erros) # site "exceções embutidas"
print(123)
raise ValuError('Deu erro') # Erros são legais para comunicação de você para o eu do futuro ou outro dev
print(456)

def divide_152(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        print('Algo que queira fazer antes')
        raise # Um pouco redundante
print(divide_152(8, 0))

# Aula 153
import sys

#sys.exit() #sai do pragrama
print(123)
print(sys.platform)

import sys as s # Mudando o nome do módulo (não recomendado)

# Aula 154 Modularização - Entendendo os seus prórpios módulos e sys.path no python
# O primeiro módulo executado chama-se __main__
# O python conhece a pasta onde o __main__ está e as pasta abaixo dele.
# Ele não reconhece todos os módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos sys.path

# import (outro.py(não foi criado)) (nome do módulo)
# print('Este módulo se chama', __name__) # (__main__)

# print(*sys.path, sep='\n')
    # (No terminal) ls (nome da pasta exibida com o comando acima de print)

# Manipulando módulos / Manipulando sys.path (Não é comum)
'''try:
    import sys
    sys.path.append('Adicionar caminho')
except:
    ...
import (nome do modulo "".py")'''

# Aula 156 Regarregando módulos, importlib e singleton
'''import importlib
import modulo

for i in range(10):
    print(i)
    import modulo # singleton
    importlib.reload(modulo) # Recarregando o modúlo
'''

# Aula 157 ... __all__
# No outro módulo, se chamar todos '*' vem somente quem está dentro do __all__
__all__ = [
    'variavel_157'
]

variavel_157 = 'Alguma coisa'

# Problemas com módulos, aula 158 e 159!!

# Aula 164 Varoáveis livres + nonlocal (locals, global)
'''def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna'''
