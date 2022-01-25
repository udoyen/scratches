import math
class Pizza:
    """
    Pizza class
    """

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes']) # returns an instance of class of type margherita

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham']) # returns an instance of class of type prosciutto

    def list_items(self):
        return self.ingredients


# Usage

print(Pizza.margherita().list_items())

print(Pizza.prosciutto().list_items())


class UyoPizza:

    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi


# Usage

p = UyoPizza(4, ['mozzarella', 'tomatoes'])

p.area()

UyoPizza.circle_area(4)