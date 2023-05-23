

def validar_nome_produto(lista_nome_produtos):
    while True:
        try:
            nome_produto = input('\nInforme o nome do produto: ').lower()
            if not nome_produto.strip():
                print('Nome do produto não pode estar vazio. Tente novamente.')
                continue
            if nome_produto in lista_nome_produtos:
                print('Nome do produto ja existe. Tente novamente.')
                continue
            # Realize outras validações, se necessário
            return nome_produto
        except ValueError:
            print('Valor inválido. Tente novamente.')
        
        
def validar_preco_produto():
    while True:
        try:
            preco_produto = float(input('Preço do produto: R$ '))
            return preco_produto
        except ValueError:
            print('Valor inválido. Tente novamente.')


def validar_quantidade_produto():
    while True:
        try:
            qtd = int(input('Quantas unidades vai levar? '))
            if qtd <= 0:
                print('Quantidade inválida. A quantidade deve ser maior que 0.')
                continue
            return qtd
        except ValueError:
            print('Valor inválido. A quantidade dever ser um número inteiro.')
            