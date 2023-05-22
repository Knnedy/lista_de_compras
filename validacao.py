

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
            if len(nome_produto) < 3 or len(nome_produto) > 50:
                print(
                    'Nome do produto deve ter entre 3 e 50 caracteres. Tente novamente.')
                continue
            # Realize outras validações, se necessário
            return nome_produto
        except ValueError:
            print('Valor inválido. Tente novamente.')
        
        
def validar_preco_produto():
    while True:
        try:
            preco_produto = float(input('Preço do produto: R$ '))
            if not isinstance(preco_produto, (int, float)):
                print('O preço do produto deve ser um valor numérico. Tente novamente.')
                continue
            if preco_produto <= 0:
                print('O preço do produto deve ser maior que zeo. Tente novamente.')
                continue
            return preco_produto
        except ValueError:
            print('Valor inválido. Tente novamente.')
