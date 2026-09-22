from models.restaurant import Restaurant
from models.menu.drink import Drink
from models.menu.plate import Plate

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
drink_juice = Drink('Suco de laranja', 5.0, 'grande')
plate_bread = Plate('Pãozinho', 2.0, 'O melhor da cidade') 
restaurant_praca.add_drink_to_menu(drink_juice)
restaurant_praca.add_plate_to_menu(plate_bread)

def main():
    print(drink_juice)
    print(plate_bread)

if __name__ == '__main__':
    main()