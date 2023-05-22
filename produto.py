def adicionar_produto(lista_nomes, lista_precos):
    nome_produto = input('Informe o nome do produto: ').lower()
    if nome_produto == '0':
        return False
    preco_produto = float(input('Preço do produto: R$ '))
    lista_nomes.append(nome_produto)
    lista_precos.append(preco_produto)
    return True


def exibir_lista_compras(lista_nomes, lista_precos):
    print(f'LISTA DE COMPRAS:')
    for nome, preco in zip(lista_nomes, lista_precos):
        print(f'Nome: {nome} | Preço: R$ {preco:.2f}')
        
        
def remover_produto(lista_nomes, lista_precos):
    nome_produto = input('\nDigite o nome do produto que deseja remover: ').lower()
    if nome_produto == '0':
        return False
    indice_produto = lista_nomes.index(nome_produto)
    lista_nomes.pop(indice_produto)
    lista_precos.pop(indice_produto)
    print(f'O produto {nome_produto} foi removido.')
    return True
