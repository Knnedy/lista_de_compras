def adicionar_produto(lista_nomes, lista_precos, lista_qtd_prod):
    nome_produto = input('Informe o nome do produto: ').lower()
    if nome_produto == '0':
        return False
    preco_produto = float(input('Preço do produto: R$ '))
    qtd = int(input('Deseja levar quantas unidades? '))
    lista_nomes.append(nome_produto)
    lista_precos.append(preco_produto)
    lista_qtd_prod.append(qtd)
    return True


def calcular_valor_total(preco, qtd):
    total = preco * qtd
    total = float(total)
    return total


def exibir_lista_compras_cliente(lista_nomes, lista_precos, lista_qtd_prod):
    print(f'LISTA DE COMPRAS:')
    for nome, preco, qtd_prod in zip(lista_nomes, lista_precos, lista_qtd_prod):
        print(f'Nome: {nome} | '
              f'Preço: R$ {preco:.2f} | '
              f'Unidades: {qtd_prod} | '
              f'Total: R$ {calcular_valor_total(preco, qtd_prod)}')
        
        
def remover_produto(lista_nomes, lista_precos):
    nome_produto = input('\nDigite o nome do produto que deseja remover: ').lower()
    if nome_produto == '0':
        return False
    indice_produto = lista_nomes.index(nome_produto)
    lista_nomes.pop(indice_produto)
    lista_precos.pop(indice_produto)
    print(f'O produto {nome_produto} foi removido.')
    return True
