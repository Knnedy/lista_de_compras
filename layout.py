def cabecalho_mini_box_online():
    msg = 'Faça seu Mercado sem sair de casa!'
    print('*' * int(len(msg) + 20))
    print(f'{msg: ^54}')
    print('*' * int(len(msg) + 20))
    print('Seja bem vindo ao nosso supermercado e fique a vontade')
    print('*' * int(len(msg) + 20))

    
def menu_opcoes():
    print('\nVeja como usar nosso sistema:\n'
          '[A] Para adicionar um produto à lista.\n'
          '[R] Para remover um produto da lista.\n'
          '[0] Para sair do programa a qualquer momento.')
    
    
def cabecalho_final():
    msg = 'Obrigado pela preferência. Volte sempre.'
    print()
    print('*' * int(len(msg) + 14))
    print(f'{msg: ^54}')
    print('*' * int(len(msg) + 14))
