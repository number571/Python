from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput

from pygments.lexers import CLexer

from os import system, popen
from re import findall

class TextEditorApp(App):
    
    def add(self, args, switch = False):
        filename = self.nameF.text
        try:
            with open(filename) as file:
                self.code.text = file.read()
        except FileNotFoundError:
            self.check.text = "Error: file not found!"
                
    def compile(self, args, result = ""):
        filename = self.nameF.text
        try:
            with open(filename, "w") as file:
                file.write(self.code.text)
            system("gcc %s"%filename)
            for string in popen("./a.out"):
                result += string
        except FileNotFoundError:
            result = "Error: file not found!"
        finally:
            self.check.text = result

    def save(self, args):
        filename = self.nameF.text
        try:
            with open(filename, "w") as file:
                result = "Success: file saved!"
                file.write(self.code.text)
        except FileNotFoundError:
            result = "Error: file not found!"
        finally:
            self.check.text = result

    def build(self):
        root = BoxLayout(
            orientation = "vertical", padding = 5)

        butn = GridLayout(
            cols = 3, size_hint = [1,.07])

        self.nameF = TextInput(
            text = "main.c", size_hint = [1,.1],
            background_color = [1,1,1,.5])
        root.add_widget(self.nameF)

        buttonA = Button(
            text = 'Add File', on_press = self.add)
        butn.add_widget(buttonA)

        buttonC = Button(
            text = 'Compile File', on_press = self.compile)
        butn.add_widget(buttonC)

        buttonS = Button(
            text = 'Save File', on_press = self.save)
        butn.add_widget(buttonS)

        root.add_widget(butn)

        self.code = CodeInput(
            text = "", lexer = CLexer())
        root.add_widget(self.code)

        self.check = TextInput(
            text = "", size_hint = [1,.3],
            background_color = [1,1,1,.5])
        root.add_widget(self.check)

        return root

if __name__ == '__main__':
    TextEditorApp().run()
