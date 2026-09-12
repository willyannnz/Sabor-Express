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

def clean_terminal_and_show_subtitle(subtitle):
    os.system('cls')
    print(subtitle)

def return_to_main_menu():
    input('Pressione qualquer tecla para voltar ao menu')
    main()

def register_restaurant():
    clean_terminal_and_show_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do restaurante: ')
    restaurants.append(restaurant_name)
    print(f'O Restaurante {restaurant_name} cadastrado com sucesso!')
    return_to_main_menu()

def list_restaurants():
    clean_terminal_and_show_subtitle('Lista de restaurantes: ')
    for restaurant in restaurants:
        print(f'- {restaurant}')
    return_to_main_menu()

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
    return_to_main_menu()

def finish_program():
    clean_terminal_and_show_subtitle('Programa finalizado com sucesso!')

def main():
    os.system('cls')
    show_program_name()
    show_menu()
    chosen_option()
if __name__ == '__main__':
    main()