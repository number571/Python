from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput

from kivy.config import Config

Config.set("graphics","resizable","0")
Config.set("graphics","width","700")
Config.set("graphics","height","500")

from re import findall
from cryptomod import *

ciphers = (
    "A1Z26 Cipher","ADFGVX Cipher","AES256-CBC Cipher",
    "Affine Cipher","Atbash Cipher","Bacon Cipher",
    "Book Cipher","Caesar Cipher","CaesarS Cipher",
    "Codes Cipher","Couples Cipher","DoubleCifir Cipher",
    "Fence Cipher","Great Cipher","Gronsfeld Cipher",
    "Hill2x2 Cipher","Hill3x3 Cipher","Homophonic Cipher",
    "Lattice Cipher","Playfair Cipher","Polibiy Cipher",
    "Ports Cipher","PowVishener Cipher","Psevdo Cipher",
    "Replace Cipher","ROT13 Cipher","Rotors Cipher","RSA Cipher",
    "Syllables Cipher","Tarabar Cipher","Trithemius Cipher",
    "Typex Cipher","Vernam Cipher","Vishener Cipher", "XOR Cipher"
)

comments = (
    "### A1Z26 ###",
    "### ADFGVX ###",
    "### AES256-CBC ###",
    "### Affine ###",
    "### Atbash ###",
    "### Bacon ###",
    "### Book ###",
    "### Caesar ###",
    "### CaesarS ###",
    "### Codes ###",
    "### Couples ###",
    "### Double Cifir ###",
    "### Fence ###",
    "### Great Cipher ###",
    "### Gronsfeld ###",
    "### Hill[2x2] ###",
    "### Hill[3x3] ###",
    "### Homophonic ###",
    "### Lattice ###",
    "### Playfair ###",
    "### Polibiy ###",
    "### Ports ###",
    "### PowVishener ###",
    "### Psevdo ###",
    "### Replace ###",
    "### ROT13 ###",
    "### Rotors ###",
    "### RSA ###",
    "### Syllables ###",
    "### Tarabar ###",
    "### Thritemius ###",
    "### Typex ###",
    "### Vernam ###",
    "### Vishener ###",
    "### XOR ###"
)

class CryptographyApp(App):

    def getCipher(self, mode):
        if mode.id in ['E','D']:
            self.result.font_size = 14
            if not self.message.text: 
                self.result.text = ":: Message is not found ::"; return
            if self.toggle[0].state == 'down':
                self.result.text = a1z26(mode.id, self.message.text)
            elif self.toggle[1].state == 'down':
                self.result.text = adfgvx(mode.id, self.message.text, self.key.text)
            elif self.toggle[2].state == 'down':
                self.result.text = aes(mode.id, self.message.text, self.key.text)
            elif self.toggle[3].state == 'down':
                self.result.text = affine(mode.id, self.message.text, self.key.text)
            elif self.toggle[4].state == 'down':
                self.result.text = atbash(self.message.text)
            elif self.toggle[5].state == 'down':
                self.result.text = bacon(mode.id, self.message.text)
            elif self.toggle[6].state == 'down':
                self.result.text = book(mode.id, self.message.text, self.key.text)
            elif self.toggle[7].state == 'down':
                self.result.text = caesar(mode.id, self.message.text, self.key.text)
            elif self.toggle[8].state == 'down':
                self.result.text = caesarS(mode.id, self.message.text, self.key.text)
            elif self.toggle[9].state == 'down':
                self.result.text = codes(mode.id, self.message.text)
            elif self.toggle[10].state == 'down':
                self.result.text = couples(self.message.text)
            elif self.toggle[11].state == 'down':
                self.result.text = doubleCifir(mode.id, self.message.text, self.key.text)
            elif self.toggle[12].state == 'down':
                self.result.text = fence(mode.id, self.message.text)
            elif self.toggle[13].state == 'down':
                self.result.text = greatcipher(mode.id, self.message.text)
            elif self.toggle[14].state == 'down':
                self.result.text = gronsfeld(mode.id, self.message.text, self.key.text)
            elif self.toggle[15].state == 'down':
                self.result.text = hill2x2(mode.id, self.message.text, self.key.text)
            elif self.toggle[16].state == 'down':
                self.result.text = hill3x3(mode.id, self.message.text, self.key.text)
            elif self.toggle[17].state == 'down':
                self.result.text = homophonic(mode.id, self.message.text)
            elif self.toggle[18].state == 'down':
                self.result.text = lattice(self.message.text)
            elif self.toggle[19].state == 'down':
                self.result.text = playfair(mode.id, self.message.text)
            elif self.toggle[20].state == 'down':
                self.result.text = polibiy(mode.id, self.message.text)
            elif self.toggle[21].state == 'down':
                self.result.text = ports(mode.id, self.message.text)
            elif self.toggle[22].state == 'down':
                self.result.text = powVishener(mode.id, self.message.text, self.key.text)
            elif self.toggle[23].state == 'down':
                self.result.text = psevdo(mode.id, self.message.text)
            elif self.toggle[24].state == 'down':
                self.result.text = replace(mode.id, self.message.text)
            elif self.toggle[25].state == 'down':
                self.result.text = rot13(self.message.text)
            elif self.toggle[26].state == 'down':
                self.result.text = rotors(mode.id, self.message.text)
            elif self.toggle[27].state == 'down':
                self.result.text = rsa(mode.id, self.message.text, self.key.text)
            elif self.toggle[28].state == 'down':
                self.result.text = syllables(mode.id, self.message.text)
            elif self.toggle[29].state == 'down':
                self.result.text = tarabar(self.message.text)
            elif self.toggle[30].state == 'down':
                self.result.text = thritemius(mode.id, self.message.text, self.key.text)
            elif self.toggle[31].state == 'down':
                self.result.text = typex(mode.id, self.message.text)
            elif self.toggle[32].state == 'down':
                self.result.text = vernam(mode.id, self.message.text, self.key.text)
            elif self.toggle[33].state == 'down':
                self.result.text = vishener(mode.id, self.message.text, self.key.text)
            elif self.toggle[34].state == 'down':
                self.result.text = xor(self.message.text, self.key.text)
        else:
            switch, code = False, ""
            self.result.font_size = 12
            self.result.text = ""
            for index in range(len(ciphers)):
                if self.toggle[index].state == 'down':
                    with open("cryptomod.py") as file:
                        for string in file:
                            if switch:
                                if comments[index] not in string:
                                    code += string
                                else: break
                            if comments[index] in string:
                                switch = True
                    self.result.text += code
        self.result.cursor = (0,0)

    def clear(self, mode):
        self.result.font_size = 14
        self.key.text = ""
        self.message.text = ""
        self.result.text = ""

    def build(self):
        root = BoxLayout(orientation = "horizontal", padding = 3)

        left = ScrollView(size_hint = [.4,1])
        right = BoxLayout(orientation = "vertical")

        leftGrid = GridLayout(cols = 1, size_hint_y = None)
        leftGrid.bind(minimum_height = leftGrid.setter('height'))

        self.toggle = [0 for _ in range(35)]

        for index in range(len(ciphers)):
            
            self.toggle[index] = ToggleButton(
                id = str(index), text = ciphers[index], 
                group = 'cipher', height = 30, 
                state = "normal", size_hint_y = None)
            leftGrid.add_widget(self.toggle[index])

        left.add_widget(leftGrid)

        topBox = BoxLayout(orientation = "horizontal", size_hint = [1,.33])

        self.key = TextInput(hint_text = "Key", multiline = False, font_size = 16)
        topBox.add_widget(self.key)

        rightTopBox = BoxLayout(orientation = "vertical", size_hint = [.5,1])
        rightTopBox.add_widget(Button(id = 'E', text = "Encrypt", on_press = self.getCipher))
        rightTopBox.add_widget(Button(id = 'D', text = "Decrypt", on_press = self.getCipher))

        topBox.add_widget(rightTopBox)
        right.add_widget(topBox)

        self.message = TextInput(hint_text = "Message", font_size = 16)
        right.add_widget(self.message)

        self.result = CodeInput(readonly = True, hint_text = "Result", font_size = 14, background_color = [1,1,1,.8])
        right.add_widget(self.result)

        downBox = BoxLayout(orientation = "horizontal", size_hint = [1,.15])

        downBox.add_widget(Button(id = 'C', text = "Code", on_press = self.getCipher))
        downBox.add_widget(Button(text = "Clear", on_press = self.clear))

        right.add_widget(downBox)

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    CryptographyApp().run()
