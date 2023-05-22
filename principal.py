from layout import cabecalho_mini_box_online, cabecalho_final, menu_opcoes
from produto import *
from validacao import *


def main():
    cabecalho_mini_box_online()
    menu_opcoes()
    
    lista_nome_produtos = []
    lista_preco_produtos = []
    
    while True:
        add_remover = input('\nDeseja Adicionar, Remover, Ver lista de produtos ou '
                            'para Sair do programa [A/R/V/S]?').lower()
        
        if add_remover == 's':
            break
            
        nome_produto = validar_nome_produto(lista_nome_produtos)
        preco_produto = validar_preco_produto()
       
        if add_remover == 'a':
            lista_nome_produtos.append(nome_produto)
            lista_preco_produtos.append(preco_produto)
            
        elif add_remover == 'r':
            if remover_produto(lista_nome_produtos, lista_preco_produtos):
                print('\nLiSTA ATUALIZADA:')
                for nome_att, preco_prod_att in zip(
                        lista_nome_produtos, lista_preco_produtos):
                    print(f'Nome: {nome_att} | '
                          f'Preço: {preco_prod_att:.2f}')
                    
        elif add_remover == 'v':
            exibir_lista_compras(lista_nome_produtos, lista_preco_produtos)
        elif add_remover == 's':
            print('Você saiu do programa.')
            break
        else:
            print('Opção inválida.')
    
    for nome_atualizado, preco_prod_atualizado in zip(lista_nome_produtos,
                                                      lista_preco_produtos):
        print(f'Nome: {nome_atualizado} | Preço: {preco_prod_atualizado:.2f}')
    
    cabecalho_final()


if __name__ == '__main__':
    main()
    