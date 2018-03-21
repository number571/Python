from kivy.app import App
from kivy.uix.button import Button
from random import randint

class ClickerApp(App):
    def click(self, args):
        self.button.text = str(int(self.button.text) + 1)
        self.button.background_color = [
            randint(0,1),
            randint(0,1),
            randint(0,1),
            randint(0,1)
        ]
    def build(self):
        self.button = Button(
            text = "0", 
            background_color = [1,1,1,1],
            on_press = self.click
        ) 
        return self.button

if __name__ == "__main__":
    ClickerApp().run()
