class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        self._name = name.title()
        self.category = category.upper()
        self._active = False
        Restaurant.restaurants.append(self)

    def __str__(self):
        return f"{self._name.ljust(20)} | {self.category.ljust(20)}"

    @classmethod
    def list_restaurants(cls):
        print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} |{"Status:"}')
        for restaurant in Restaurant.restaurants:
            print(f'-{restaurant._name.ljust(20)} |{restaurant.category.ljust(20)} |{restaurant.active}')

    @property
    def active(self):
        return '✅' if self._active else '❌'

    def alter_activate(self):
        self._active = not self._active

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_praca.alter_activate()
restaurant_pizza = Restaurant('Pizzaria Express', 'Pizza')

Restaurant.list_restaurants()
