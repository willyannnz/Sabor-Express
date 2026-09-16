class Restaurant:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.active = False

    def __str__(self):
        return f"{self.name.ljust(20)} | {self.category.ljust(20)}"

restaurant_praca = Restaurant('Restaurante da Praça', 'Comida Caseira')
restaurant_pizza = Restaurant('Pizzaria Express', 'Pizza')

print(restaurant_praca)
print(restaurant_pizza)
