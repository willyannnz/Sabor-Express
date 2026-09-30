from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_praca.apply_discount()
drink_juice = Drink('Suco de laranja', 5.0, 'grande')
dish_bread = Dish('Pãozinho', 2.0, 'O melhor da cidade') 
restaurant_praca.add_to_the_menu(drink_juice)
restaurant_praca.add_to_the_menu(dish_bread)

def main():
    restaurant_praca.show_menu

if __name__ == '__main__':
    main()  