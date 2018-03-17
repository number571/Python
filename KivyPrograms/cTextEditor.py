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
        self.root = BoxLayout(
            orientation = "vertical", 
            padding = 5)

        self.butn = GridLayout(
            cols = 3, size_hint = [1,.07])

        self.nameF = TextInput(
            text = "main.c",
            size_hint = [1,.1],
            background_color = [1,1,1,.5])
        self.root.add_widget(self.nameF)

        self.buttonA = Button(
            text = 'Add File',
            on_press = self.add)
        self.butn.add_widget(self.buttonA)

        self.buttonC = Button(
            text = 'Compile File',
            on_press = self.compile)
        self.butn.add_widget(self.buttonC)

        self.buttonS = Button(
            text = 'Save File',
            on_press = self.save)
        self.butn.add_widget(self.buttonS)

        self.root.add_widget(self.butn)

        self.code = CodeInput(
            text = "",lexer = CLexer())
        self.root.add_widget(self.code)

        self.check = TextInput(
            text = "",size_hint = [1,.3],
            background_color = [1,1,1,.5])
        self.root.add_widget(self.check)

        return self.root

if __name__ == '__main__':
    TextEditorApp().run()
