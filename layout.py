def cabecalho_mini_box_online():
    msg = 'FAÇA SUAS COMPRAS DE MERCADO SEM SAIR DE CASA'
    print('*' * int(len(msg) + 20))
    print(f'{msg: ^67}')
    print('*' * int(len(msg) + 20))
    msg2 = 'SEJA BEM VINDO E VOLTE SEMPRE'
    print(f'{msg2: ^67}')
    print('*' * int(len(msg) + 20))

    
def menu_opcoes():
    print('\n[A] adicionar um produto à lista.\n'
          '[R] remover um produto da lista.\n'
          '[V] ver a sua lista.\n'
          '[S] sair do programa.')
    
    
def msg_lista_compras():
    msg = 'SUA LISTA DE COMPRAS:'
    print('*' * int(len(msg) + 44))
    print(f'{msg: ^69}')
    print('*' * int(len(msg) + 44))


def msg_lista_compras_atualizada():
    msg = 'SUA LISTA DE COMPRAS ATUALIZADA:'
    print('*' * int(len(msg) + 33))
    print(f'{msg: ^71}')
    print('*' * int(len(msg) + 33))
    

def cabecalho_final():
    msg = 'OBRIGADO PELA PREFERÊNCIA. VOLTE SEMPRE.'
    print()
    print('*' * int(len(msg) + 25))
    print(f'{msg: ^67}')
    print('*' * int(len(msg) + 25))
