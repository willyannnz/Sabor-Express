import os

restaurants = [{'nome': 'Bico de brasa', 'categoria': 'Comida Brasileira', 'ativo': True}, 
               {'nome': 'Pizza Suprema', 'categoria': 'Pizzas', 'ativo': False},
               {'nome': 'Sabor da Terra', 'categoria': 'Comida Brasileira', 'ativo': False}]

def show_program_name():
    """This function displays the name of the program in a stylized format.
    
    inputs:
        - None
        
    outputs:
        - Prints the program name in a stylized format to the console.
    
    """


    print("""

    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)

def show_menu():
    """This function displays the main menu options for the restaurant management system.
    
    inputs:
        - None
    
    outputs:
        - Prints the main menu options to the console, allowing the user to choose an action (register a restaurant, list restaurants, toggle restaurant status, or exit the program).
    
    """
    
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def clean_terminal_and_show_subtitle(subtitle):
    """This function clears the terminal and displays a subtitle for the current action being performed in the restaurant management system.
    
    inputs:
        - subtitle (str): The subtitle to be displayed for the current action.

    outputs:
        - Clears the terminal and prints the subtitle in a stylized format to indicate the current action
    
    """


    os.system('cls')
    line = '=' * (len(subtitle))
    print(line)
    print(subtitle)
    print(line)

def return_to_main_menu():
    input('\nPressione qualquer tecla para voltar ao menu')
    main()

def register_restaurant():
    """This function registers a new restaurant in the system.
    
    Inputs:
        - restaurant_name (str): The name of the restaurant.
        - category (str): The category of the restaurant.
    Outputs:
        - Adding a new restaurant to the restaurants list and displaying a success message.
    
    """
    clean_terminal_and_show_subtitle('Cadastro de novos restaurantes')
    restaurant_name = input('Digite o nome do restaurante: ')
    category = input('Digite a categoria do restaurante: ')
    data_restaurant = {'nome': restaurant_name, 'categoria': category, 'ativo': False}
    restaurants.append(data_restaurant)
    print(f'O Restaurante {restaurant_name} cadastrado com sucesso!')
    return_to_main_menu()

def list_restaurants():
    """This function lists all registered restaurants.
    
    inputs:
        - None

    Outputs:
        - Displays the name, category, and status (active/inactive) of each restaurant in the system.
    
    """
    clean_terminal_and_show_subtitle('Lista de restaurantes: ')
    print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} |{"Status:"}')
    for restaurant in restaurants:
        restaurant_name = restaurant['nome']
        restaurant_category = restaurant['categoria']
        restaurant_status = 'Ativo' if restaurant['ativo'] else 'Inativo'
        print(f'-{restaurant_name.ljust(20)} |{restaurant_category.ljust(20)} |{restaurant_status}')
    return_to_main_menu()

def activate_restaurant():
    """This function toggles the active status of a restaurant based on user input.
    
    inputs:
        - restaurant_name (str): The name of the restaurant to toggle its status.

    Outputs:
        - Displays a message indicating if the restaurant was activated or deactivated successfully, or if it was not found in the system.
    
    """

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
    """
    This function prompts the user to choose an option from the main menu and executes the corresponding action based on the user's input.

    Inputs:
        - chosen_option (int): The option chosen by the user from the main menu.
    
    Outputs:
        - Executes the corresponding function based on the chosen option (register_restaurant, list_restaurants, activate_restaurant, finish_program) or displays an error message if the option is invalid.
    """
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
    """
    This function handles the case when the user selects an invalid option from the main menu.

    inputs:
        - None

    outputs:
        - Displays an error message indicating that the chosen option is invalid and returns to the main menu
    """
    print('Opção inválida')
    return_to_main_menu()

def finish_program():
    """
    This function handles the case when the user chooses to finish the program.

    Inputs:
        - None

    outputs:
        - Displays a success message indicating that the program has finished successfully and exits the program.
    """
    clean_terminal_and_show_subtitle('Programa finalizado com sucesso!')

def main():
    """This function serves as the entry point of the program. It clears the terminal, displays the program name, shows the main menu, and prompts the user to choose an option.
    
    Inputs:
        - None

    Outputs:
        - Executes the main program flow by calling the necessary functions to display the program name, show the main menu, and handle user input for choosing an option.
    """
    os.system('cls')
    show_program_name()
    show_menu()
    chosen_option()
if __name__ == '__main__':
    main()