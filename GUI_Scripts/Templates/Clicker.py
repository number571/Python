from kivy.app import App
from kivy.uix.button import Button
from random import random

class ClickerApp(App):
    def click(self, args):
        self.button.text = str(int(self.button.text) + 1)
        self.button.background_color = [
            random(),
            random(),
            random(),
            random()
        ]
    def build(self):
        self.button = Button(
            text = "0", 
            font_size = 30,
            background_color = [1,1,1,1],
            on_press = self.click
        ) 
        return self.button

if __name__ == "__main__":
    ClickerApp().run()
