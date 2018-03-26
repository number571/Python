from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

from kivy.config import Config
Config.set("graphics","resizable","0")
Config.set("graphics","width","750")
Config.set("graphics","height","600")

from re import findall

ciphers = (
    "A1Z26 Cipher","ADFGVX Cipher","AES Cipher",
    "Affine Cipher","Atbash Cipher","Bacon Cipher",
    "Book Cipher","Caesar Cipher","CaesarS Cipher",
    "Codes Cipher","Couples Cipher","CubeVishener Cipher",
    "DoubleCifir Cipher","En-Ru Cipher","Fence Cipher",
    "Gronsfeld Cipher","Hill2x2 Cipher","Hill3x3 Cipher",
    "Homophonic Cipher","Lattice Cipher","Playfair Cipher",
    "Polibiy Cipher","Ports Cipher","Psevdo Cipher",
    "Replace Cipher","ROT13 Cipher","Rotors Cipher",
    "RSA Cipher","Syllables Cipher","Tarabar Cipher",
    "Trithemius Cipher","Typex Cipher","Vernam Cipher",
    "Vishener Cipher", "XOR Cipher"
)

def a1z26_regular(text):
    template = r"[0-9]+"
    return findall(template, text)

def a1z26(mode, message, final = ""):
    message = message.upper()
    alpha = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if mode == 'E': 
        for symbol in message:
            if symbol not in [chr(x) for x in range(65,91)]:
                message = message.replace(symbol, '')
        for symbol in message:
            final += "%hu "%(alpha.index(symbol)+1)
    else: 
        for number in a1z26_regular(message):
            final += "%s"%alpha[int(number)-1]
    return final

class CryptographyApp(App):

    def getCipher(self, args):
        if self.toggle[0].state == 'down': 
            self.result.text = a1z26(args.id, self.message.text)

    def getInfo(self, args):
        info = {
            '0':'''
    The key is not needed.
    Encrypt: A = 1, B = 2, C = 3, ... X = 24, Y = 25, Z = 26.
    Decrypt: 1 = A, 2 = B, 3 = C, ... 24 = X, 25 = Y, 26 = Z.''',
            '1':"",
            '2':"",
            '3':"",
            '4':"",
            '5':"",
            '6':"",
            '7':"",
            '8':"",
            '9':"",
            '10':"",
            '11':"",
            '12':"",
            '13':"",
            '14':"",
            '15':"",
            '16':"",
            '17':"",
            '18':"",
            '19':"",
            '20':"",
            '21':"",
            '22':"",
            '23':"",
            '24':"",
            '25':"",
            '26':"",
            '27':"",
            '28':"",
            '29':"",
            '30':"",
            '31':"",
            '32':"",
            '33':"",
            '34':""
        }
        self.result.text = info[args.id]

    def build(self):
        root = BoxLayout(orientation = "horizontal", padding = 5)

        left = ScrollView(size_hint = [.4,1])
        right = BoxLayout(orientation = "vertical")

        leftGrid = GridLayout(cols = 2, size_hint_y = None)
        leftGrid.bind(minimum_height = leftGrid.setter('height'))

        self.toggle = [0 for _ in range(35)]

        for index in range(len(ciphers)):
            
            self.toggle[index] = ToggleButton(
                id = str(index), text = ciphers[index], 
                group = 'cipher', height = 30, 
                state = "normal",size_hint_y = None)
            leftGrid.add_widget(self.toggle[index])

            leftGrid.add_widget(Button(
                id = str(index), text = "<- Info", 
                height = 30, size_hint = [.4,1], 
                size_hint_y = None, on_press = self.getInfo))

        left.add_widget(leftGrid)

        rigthGrid = GridLayout(cols = 2, size_hint = [1,.155])

        rigthGrid.add_widget(Button(id = 'E', text = "Encrypt", on_press = self.getCipher))
        rigthGrid.add_widget(Button(id = 'D', text = "Decrypt", on_press = self.getCipher))

        right.add_widget(rigthGrid)

        right.add_widget(TextInput(hint_text = "Key[s] for Cipher", size_hint = [1,.155]))

        self.message = TextInput(hint_text = "Encrypt/Decrypt the message")
        right.add_widget(self.message)

        self.result = TextInput(readonly = True, hint_text = "Result of Encryption/Decryption", background_color = [1,1,1,.8])
        right.add_widget(self.result)

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    CryptographyApp().run()
