from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")

saveInput = ""

class CalculatorApp(App):

    def calculate(self, symbol):
        global saveInput
        if symbol.text is '<':
            saveInput = self.result.text = ""
        elif symbol.text is not '=':
            self.result.text += symbol.text
            saveInput += symbol.text
        else:
            try: saveInput = self.result.text = str(eval(saveInput))
            except: saveInput = self.result.text = ""
        
    def build(self):
        root = BoxLayout(orientation = "vertical", padding = 5)

        self.result = TextInput(
            text = "", readonly = True, font_size = 25, 
            size_hint = [1,.75], background_color = [1,1,1,.8])
        root.add_widget(self.result)

        allButtons = GridLayout(cols = 5)

        allButtons.add_widget(Button(text = '7', on_press = self.calculate))
        allButtons.add_widget(Button(text = '8', on_press = self.calculate))
        allButtons.add_widget(Button(text = '9', on_press = self.calculate))
        allButtons.add_widget(Button(text = "+", on_press = self.calculate))
        allButtons.add_widget(Button(text = "<", on_press = self.calculate))

        allButtons.add_widget(Button(text = '4', on_press = self.calculate))
        allButtons.add_widget(Button(text = '5', on_press = self.calculate))
        allButtons.add_widget(Button(text = '6', on_press = self.calculate))
        allButtons.add_widget(Button(text = "-", on_press = self.calculate))
        allButtons.add_widget(Button(text = "(", on_press = self.calculate))

        allButtons.add_widget(Button(text = '1', on_press = self.calculate))
        allButtons.add_widget(Button(text = '2', on_press = self.calculate))
        allButtons.add_widget(Button(text = '3', on_press = self.calculate))
        allButtons.add_widget(Button(text = "*", on_press = self.calculate))
        allButtons.add_widget(Button(text = ")", on_press = self.calculate))

        allButtons.add_widget(Button(text = '0', on_press = self.calculate))
        allButtons.add_widget(Button(text = ".", on_press = self.calculate))
        allButtons.add_widget(Button(text = "=", on_press = self.calculate))
        allButtons.add_widget(Button(text = "/", on_press = self.calculate))
        allButtons.add_widget(Button(text = "%", on_press = self.calculate))

        root.add_widget(allButtons)
        return root

if __name__ == "__main__":
    CalculatorApp().run()
