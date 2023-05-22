from layout import cabecalho_mini_box_online, cabecalho_final, menu_opcoes
from produto import *
from validacao import *


def main():
    cabecalho_mini_box_online()
    menu_opcoes()
    
    lista_nome_produtos = []
    lista_preco_produtos = []
    lista_qtd_prod = []
    
    while True:
        nome_produto = validar_nome_produto(lista_nome_produtos)
        if not nome_produto:
            break
        
        preco_produto = validar_preco_produto()
        qtd_produto = validar_quantidade_produto()
        
        # calcular_valor_total(preco_produto, qtd_produto)
        
        lista_nome_produtos.append(nome_produto)
        lista_preco_produtos.append(preco_produto)
        lista_qtd_prod.append(qtd_produto)
        
        while True:
            add_remover = input('Escolha uma das opções: ').lower()
            if add_remover == 'a':
                break
            elif add_remover == 'r':
                if remover_produto(lista_nome_produtos, lista_preco_produtos):
                    print('\nLiSTA ATUALIZADA:')
                    for nome_att, preco_prod_att, unidades_produto in zip(
                            lista_nome_produtos, lista_preco_produtos, lista_qtd_prod):
                        print(f'Nome: {nome_att} | '
                              f'Preço: {preco_prod_att:.2f}'
                              f'Unidades: {unidades_produto}'
                              f'Total: R$ {lista_preco_produtos * unidades_produto}')
                        break
                else:
                    continue
            elif add_remover == 'v':
                exibir_lista_compras_cliente(lista_nome_produtos,
                                             lista_preco_produtos,
                                             lista_qtd_prod)
                calcular_valor_total(preco_produto, qtd_produto)
            elif add_remover == 's':
                print('Você saiu do programa.')
                break
            else:
                print('Opção inválida.')
            
        if add_remover == 's':
            break
            
    cabecalho_final()
    

if __name__ == '__main__':
    main()
    