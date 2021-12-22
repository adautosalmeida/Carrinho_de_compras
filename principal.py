produtos_carrinho = []  # lista onde será armazenado os produtos

def imprimi_produtos_carrinho():
    if len(produtos_carrinho) <= 0:
        print('>>>>> Carrinho vazio <<<<<')
        print()

    for  itens in produtos_carrinho:
        print(f' Produto: {itens}')  # faz com que o índice inicie sua contagem em 1 ao invés de 0

def incluir_produtos_carrinho():
    print('>>>>> Entre com os produto que deseja adicionar: ')
    produtos_carrinho.append(input())
    while True:
        print('>>>>> Deseja adicionar outro produto? ')
        print('[1] - SIM\n[2] - NAO')
        resposta = input()
        if resposta == '1':
            print('>>>>> Entre com os produto que deseja adicionar: ')
            produtos_carrinho.append(input())
        elif resposta == '2':
            print('>>>>> Retornando ao Menu... <<<<<')
            break
        else:
            print('Opção Inválida')

def excluir_produtos_carrinhos():
    try:

        if len(produtos_carrinho) <= 0:
            print('>>>>> Carrinho vazio, não há o que excluir ')
            print()
        else:
            print('>>>>>> Entre com os produtos que deseja excluir: ')
            produtos_carrinho.remove(input())


            while True:
                print('>>>>> Deseja remover outro produto? ')
                print('[1] - SIM\n[2] - NAO')
                resposta = input()
                if resposta == '1':
                    print('>>>>> Entre com os produtos que deseja excluir: ')
                    produtos_carrinho.remove(input())
                    print('Produto removido com sucesso.')
                elif resposta == '2':
                    print('>>>>> Retornando ao Menu... <<<<<')
                    break

                else:
                    print('Opção Inválida')

    except ValueError:
        if len(produtos_carrinho) <= 0:
            print('>>>>> Carrinho vazio, não há o que excluir ')
        else:
            if produtos_carrinho not in produtos_carrinho:
                print('Não existe esse produto no carrinho.')
    except ValueError:
        print('Um erro inesperado ocorreu. Tente novamente.')






def mensagem_de_agradecimento():
    print()
    print('>>>>> FECHANDO SEU PEDIDO E IMPRIMINDO SEUS ITENS... <<<<<')
    imprimi_produtos_carrinho() # tirar isso daqui
    print('>>>>> OBRIGADO PELA PREFERENCIA E VOLTE SEMPRE <<<<< ')
    print()



def imprimir_menu():

    print('============================================================================')
    print('                            * MENU *                                        ')
    print('============================================================================')
    print(' 1 - Mostrar itens do carrinho.                                             ')
    print(' 2 - Adicionar itens ao carrinho.                                           ')
    print(' 3 - Excluir itens do carrinho.                                             ')
    print(' 0 - Encerrar programa.                                                     ')
    print('============================================================================')


while True:
    imprimir_menu()
    print()

    opcao = input('>>>>> Escolha uma opção: ')
    print()
    if opcao == '1':
        imprimi_produtos_carrinho()
    elif opcao == '2':
        incluir_produtos_carrinho()
    elif opcao == '3':
        excluir_produtos_carrinhos()
    elif opcao == '0':
        mensagem_de_agradecimento()
        break
    else:
        print('Opção Inválida')
