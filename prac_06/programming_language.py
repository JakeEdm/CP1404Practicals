"""Programming Language Class"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection=None, year=0):
        """Initialises a language instance"""
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Checks if language is dynamically typed"""
        return self.typing == "Dynamic"
