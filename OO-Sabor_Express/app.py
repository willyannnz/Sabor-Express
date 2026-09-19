from modelos.restaurant import Restaurant

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_praca.get_review('Gui', 10)
restaurant_praca.get_review('Lais', 8)
restaurant_praca.get_review('Evelyn', 5)



def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main()