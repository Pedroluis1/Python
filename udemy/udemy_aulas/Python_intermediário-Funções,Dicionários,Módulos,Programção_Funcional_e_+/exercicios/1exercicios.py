import copy
# Exercícios 
# Fazer exercicios 160, 161, 162, 163, 140, 131, 132, 125, 169, 170, 171, 172, 

# Aumente os preços dos produtos a seguir em 10%
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print(**produtos for chave, valor in produtos)

produtos = [
    {**produtos, 'preco': produtos['preco'] * 0,1}
    for produtos in produtos
]

print(**produtos for chave, valor in produtos)

# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(produtos)

# Ordene os produtos por nome decrescente (do maior para menor)
print(novos_produtos.sort(key=lambda item: item['nome'], reverse=True))

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
print(novos_produtos.sort(key=lambda item: item['preco'], reverse=True))

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
