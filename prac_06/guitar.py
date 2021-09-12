"""Module docstring"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Creates a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Gets age of the guitar"""
        return 2021 - self.year

    def is_vintage(self):
        """Checks if guitar is 50 or more years old"""
        return Guitar.get_age(self) >= 50
