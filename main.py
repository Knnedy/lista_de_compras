from layout import *
from produto import *
from validacao import *
from listas import *


def main():
    cabecalho_mini_box_online()
    while True:
        while True:
            menu_opcoes()
            add_remover = input('Escolha uma das opções: ')
            if add_remover == 'a':
                nome_produto = validar_nome_produto(lista_nome_produtos)
                if not nome_produto:
                    break
            
                preco_produto = validar_preco_produto()
                qtd_produto = validar_quantidade_produto()
                valor_total_compras = calcular_valor_total_por_produto(preco_produto,
                                                                       qtd_produto)

                lista_nome_produtos.append(nome_produto)
                lista_preco_produtos.append(preco_produto)
                lista_qtd_prod.append(qtd_produto)
                lista_valor_total_produtos.append(valor_total_compras)

            elif add_remover == 'r':
                remover_produto(lista_nome_produtos, lista_preco_produtos, lista_qtd_prod)
                exibir_lista_compras_cliente(lista_nome_produtos, lista_preco_produtos,
                                             lista_qtd_prod)
                valor_total = calcular_valor_total(lista_preco_produtos, lista_qtd_prod)
                print(f'Total das compras: {valor_total:.2f}')
                continue
            elif add_remover == 'v':
                msg_lista_compras()
                exibir_lista_compras_cliente(lista_nome_produtos, lista_preco_produtos,
                                             lista_qtd_prod)
                valor_total = calcular_valor_total(lista_preco_produtos, lista_qtd_prod)
                print(f'Total das compras: {valor_total:.2f}')
            elif add_remover == 's':
                msg_lista_compras()
                exibir_lista_compras_cliente(lista_nome_produtos, lista_preco_produtos,
                                             lista_qtd_prod)
                valor_total = calcular_valor_total(lista_preco_produtos, lista_qtd_prod)
                print(f'Total das compras: {valor_total:.2f}')
                break
            else:
                print('Opção inválida.')
        if add_remover == 's':
            break
        
    cabecalho_final()
    

if __name__ == '__main__':
    main()
    