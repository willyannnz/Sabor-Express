import os

restaurants = ['Pizzaria do Zé', 'Churrascaria do João', 'Restaurante da Maria']

def show_program_name():
    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def show_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def register_restaurant():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    restaurant_name = input('Digite o nome do restaurante: ')
    restaurants.append(restaurant_name)
    print(f'O Restaurante {restaurant_name} cadastrado com sucesso!')
    input('Pressione qualquer tecla para voltar ao menu principal...')
    main()

def list_restaurants():
    os.system('cls')
    print('Lista de restaurantes:\n')
    for restaurant in restaurants:
        print(f'- {restaurant}')
    input('\nPressione qualquer tecla para voltar ao menu principal...')
    main()

def chosen_option():
    try:
        chosen_option = int(input('Digite a opção desejada: '))
        print(f'Opção escolhida: {chosen_option}')
        if chosen_option == 1:
            register_restaurant()
        elif chosen_option == 2:
            list_restaurants()
        elif chosen_option == 3:
            print('Ativar restaurante')
        elif chosen_option == 4:
            finish_program()
        else:
            option_not_found()
    except ValueError:
        option_not_found()

def option_not_found():
    print('Opção inválida')
    input('Pressione qualquer tecla para voltar ao menu principal...')
    main()

def finish_program():
    os.system('cls')
    # os.system('clear') in macOS ou Linux
    print('Finalizando app...')

def main():
    os.system('cls')
    show_program_name()
    show_menu()
    chosen_option()
if __name__ == '__main__':
    main()