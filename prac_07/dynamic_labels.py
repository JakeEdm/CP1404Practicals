"""Dynamic Labels"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label
from random import randint


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Jake", "Billy-Joe", "Samuel", "Devon", "Victoria"]
        # self.other_names = ["Samson", "Jack", "Peter", "Gary", "Roger"]

    def build(self):
        """"Build the Kivy GUI"""
        Window.size = (800, 800)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.generate_labels()
        return self.root

    def generate_labels(self):
        """Generates a label for every name in list"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)

    # def add_random_name(self):
    #     random_name = self.other_names[randint(0, len(self.other_names) - 1)]
    #     label = Label(text=random_name)
    #     self.root.ids.entries_box.add_widget(label)

    # def clear_all(self):
    #     self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
