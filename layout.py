def cabecalho_mini_box_online():
    msg = 'Faça seu Mercado sem sair de casa!'
    print('*' * int(len(msg) + 20))
    print(f'{msg: ^54}')
    print('*' * int(len(msg) + 20))
    print('Seja bem vindo ao nosso supermercado e fique a vontade')
    print('*' * int(len(msg) + 20))

    
def menu_opcoes():
    print('\n[A] adicionar um produto à lista.\n'
          '[R] remover um produto da lista.\n'
          '[V] ver a sua lista.\n'
          '[S] sair do programa.')
    
    
def cabecalho_final():
    msg = 'Obrigado pela preferência. Volte sempre.'
    print()
    print('*' * int(len(msg) + 14))
    print(f'{msg: ^54}')
    print('*' * int(len(msg) + 14))
