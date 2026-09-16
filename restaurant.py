class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name.ljust(20)} | {self.category.ljust(20)}"

    def list_restaurants():
        print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} |{"Status:"}')
        for restaurant in Restaurant.restaurants:
            restaurant_name = restaurant.name
            restaurant_category = restaurant.category
            restaurant_status = 'Ativo' if restaurant.active else 'Inativo'
            print(f'-{restaurant_name.ljust(20)} |{restaurant_category.ljust(20)} |{restaurant_status}')

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_pizza = Restaurant('Pizzaria Express', 'Pizza')

Restaurant.list_restaurants()
