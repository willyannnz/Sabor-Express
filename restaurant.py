class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self.name.ljust(20)} | {self.category.ljust(20)}"
    
    def list_restaurants():
        print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} |{"Status:"}')
        for restaurant in Restaurant.restaurants:
            print(f'-{restaurant.name.ljust(20)} |{restaurant.category.ljust(20)} |{restaurant.active}')

    @property
    def active(self):
        return '✅' if self._active else '❌'

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_pizza = Restaurant('Pizzaria Express', 'Pizza')

Restaurant.list_restaurants()
