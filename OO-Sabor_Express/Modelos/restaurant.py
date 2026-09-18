class Restaurant:

    restaurants = [] # shared list that stores every Restaurant instance created

    def __init__(self, name, category):
        self._name = name.title() # restaurant name, formatted (Title Case)
        self.category = category.upper() # restaurant category, formatted (UPPERCASE)
        self._active = False # active status, starts as inactive
        Restaurant.restaurants.append(self) # auto-register this instance in the shared list

    def __str__(self):
        # defines how the object is displayed when printed
        return f"{self._name.ljust(20)} | {self.category.ljust(20)}"

    @classmethod
    def list_restaurants(cls):
        # prints all restaurants stored in the shared list, formatted as a table
        print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} |{"Status:"}')
        for restaurant in Restaurant.restaurants:
            print(f'-{restaurant._name.ljust(20)} |{restaurant.category.ljust(20)} |{restaurant.active}')

    @property
    def active(self):
        # returns a readable status (✅/❌) based on the internal _active flag
        return '✅' if self._active else '❌'

    def alter_status(self):
         # toggles the restaurant's active status (True <-> False)
        self._active = not self._active
