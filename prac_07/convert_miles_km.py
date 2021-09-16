"""Module docstring"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILE_IN_KILOMETRES = 1.60934


class ConvertMilesToKm(App):
    output_km = StringProperty()

    def build(self):
        """Convert miles to km"""
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, string):
        """Handles calculation from miles to km"""
        miles = self.convert_to_float(string)
        self.output_km = str(miles * MILE_IN_KILOMETRES)

    def handle_increment(self, current_number, increment):
        """Changes number in text box according to input"""
        try:
            new_number = float(current_number) + increment
            self.root.ids.input_miles.text = str(new_number)
        # handles trying to increment an invalid input
        except ValueError:
            new_number = float(0) + increment
            self.root.ids.input_miles.text = str(new_number)

    @staticmethod
    def convert_to_float(value):
        """Convert string to float value, display 0.0 is invalid"""
        try:
            return float(value)
        except ValueError:
            return 0.0


ConvertMilesToKm().run()
