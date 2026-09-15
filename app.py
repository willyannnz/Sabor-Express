import os

restaurants = [{'nome': 'Bico de brasa', 'categoria': 'Comida Brasileira', 'ativo': True}, 
               {'nome': 'Pizza Suprema', 'categoria': 'Pizzas', 'ativo': False},
               {'nome': 'Sabor da Terra', 'categoria': 'Comida Brasileira', 'ativo': False}]

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
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def clean_terminal_and_show_subtitle(subtitle):
    os.system('cls')
    line = '-' * (len(subtitle))
    print(line)
    print(subtitle)
    print(line)

def return_to_main_menu():
    input('Pressione qualquer tecla para voltar ao menu')
    main()

def register_restaurant():
    clean_terminal_and_show_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do restaurante: ')
    category = input('Digite a categoria do restaurante: ')
    data_restaurant = {'nome': restaurant_name, 'categoria': category, 'ativo': False}
    restaurants.append(data_restaurant)
    print(f'O Restaurante {restaurant_name} cadastrado com sucesso!')
    return_to_main_menu()

def list_restaurants():
    clean_terminal_and_show_subtitle('Lista de restaurantes: ')
    for restaurant in restaurants:
        restaurant_name = restaurant['nome']
        restaurant_category = restaurant['categoria']
        restaurant_status = 'Ativo' if restaurant['ativo'] else 'Inativo'
        print(f'Nome: {restaurant_name.ljust(20)} | Categoria: {restaurant_category.ljust(20)} | Status: {restaurant_status}')
    return_to_main_menu()

def activate_restaurant():
    clean_terminal_and_show_subtitle('Alternando estado do restaurante')
    restaurant_name = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurant_finded = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['nome']:
            restaurant_finded = True
            restaurant['ativo'] = not restaurant['ativo']
            message = f'O restaurante {restaurant_name} foi ativado com sucesso!' if restaurant['ativo'] else f'O restaurante {restaurant_name} foi desativado com sucesso!'
            print(message)
    if not restaurant_finded:
        print(f'O restaurante {restaurant_name} não foi encontrado!')

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
            activate_restaurant()
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