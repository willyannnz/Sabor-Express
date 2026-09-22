from models.review import Review

class Restaurant:
    """Represents a restaurant, with a name, category, status and reviews."""

    restaurants = []  # shared list that stores every Restaurant instance created

    def __init__(self, name, category):
        """Creates a new restaurant and adds it to the shared list.

        Args:
            name (str): the restaurant's name.
            category (str): the restaurant's category.
        """
        self._name = name.title()  # restaurant name, formatted (Title Case)
        self.category = category.upper()  # restaurant category, formatted (UPPERCASE)
        self._active = False  # active status, starts as inactive
        self._review = []  # here will stores the reviews
        self._menu = [] # This will stores the menu itens
        Restaurant.restaurants.append(self)  # auto-register this instance in the shared list

    def __str__(self):
        """Returns the text shown when the restaurant is printed.

        Returns:
            str: the restaurant's name and category, formatted.
        """
        return f"{self._name.ljust(20)} | {self.category.ljust(20)}"

    @classmethod
    def list_restaurants(cls):
        """Prints all restaurants from the shared list as a table."""
        print(f'{"Nome do restaurante:".ljust(21)} |{"Categoria:".ljust(20)} | {"Avaliação:".ljust(20)} |{"Status:"}')
        for restaurant in Restaurant.restaurants:
            print(f'-{restaurant._name.ljust(20)} |{restaurant.category.ljust(20)} | {str(restaurant.average_rating).ljust(20)} |{restaurant.active}')

    @property
    def active(self):
        """Returns an icon showing if the restaurant is active or not.

        Returns:
            str: '✅' if active, '❌' if not active.
        """
        return '✅' if self._active else '❌'

    def alter_status(self):
        """Switches the restaurant's status between active and inactive."""
        self._active = not self._active

    def get_review(self, costumer, rating):
        """Creates a Review and adds it to this restaurant, if the rating is valid.

        Args:
            costumer (str): the name of the person leaving the review.
            rating (int): the rating, must be between 1 and 5.
        """
        if 0 < rating <= 5:
            review = Review(costumer, rating)
            self._review.append(review)

    @property
    def average_rating(self):
        """Returns the average of all ratings given to this restaurant.

        Returns:
            float or str: the average rating, or '-' if there are no reviews yet.
        """
        if not self._review:
            return '-'
        sum_of_the_ratings = sum(review._rating for review in self._review)
        quantity_of_ratings = len(self._review)
        average = round(sum_of_the_ratings / quantity_of_ratings, 1)
        return average

    def add_drink_to_menu(self, drink):
        self._menu.append(drink)

    def add_plate_to_menu(self, plate):
        self._menu.append(plate)