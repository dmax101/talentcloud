lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores']

# Atualizar a lista de produtos
lista_produtos[1] = 'rímel'  # Substituir 'batons' por 'rímel'
lista_produtos[4] = 'cremes hidratantes'  # Substituir 'loções' por 'cremes hidratantes'
del lista_produtos[7]  # Remover 'delineadores'

# Adicionar dois novos produtos à lista
lista_produtos.append('sombra para os olhos')
lista_produtos.append('base líquida')

# Imprimir a nova lista de produtos
# Iterar sobre a lista de produtos
for produto in lista_produtos:
    # Imprimir a frase com o produto
    print("Temos", produto, "à venda!")
