from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.dish import Dish

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
drink_juice = Drink('Suco de laranja', 5.0, 'grande')
drink_juice.apply_discount()
dish_bread = Dish('Pãozinho', 2.0, 'O melhor da cidade') 
dish_bread.apply_discount()
restaurant_praca.add_to_the_menu(drink_juice)
restaurant_praca.add_to_the_menu(dish_bread)

def main():
    restaurant_praca.show_menu

if __name__ == '__main__':
    main()  