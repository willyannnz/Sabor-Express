from modelos.restaurant import Restaurant

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_pizza = Restaurant('Pizzaria Express', 'Pizza')
restaurant_mexicano = Restaurant('Mexicano Food', 'Mexicana')

restaurant_mexicano.alter_status()

def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()