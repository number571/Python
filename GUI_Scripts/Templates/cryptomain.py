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

from cryptoPy import *

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

class CryptographyApp(App):

    def getCipher(self, args):
        if self.toggle[0].state == 'down': 
            self.result.text = a1z26(args.id, self.message.text)
        elif self.toggle[1].state == 'down':
            self.result.text = adfgvx(args.id, self.message.text, self.key.text)
        elif self.toggle[2].state == 'down':
            self.result.text = aes(args.id, self.message.text, self.key.text)
        elif self.toggle[3].state == 'down':
            self.result.text = affine(args.id, self.message.text, self.key.text)
        elif self.toggle[4].state == 'down':
            self.result.text = atbash(self.message.text)
        elif self.toggle[5].state == 'down':
            self.result.text = bacon(args.id, self.message.text)
        elif self.toggle[6].state == 'down':
            self.result.text = book(args.id, self.message.text, self.key.text)
        elif self.toggle[7].state == 'down':
            self.result.text = caesar(args.id, self.message.text, self.key.text)
        elif self.toggle[8].state == 'down':
            self.result.text = caesarS(args.id, self.message.text, self.key.text)
        elif self.toggle[9].state == 'down':
            self.result.text = codes(args.id, self.message.text)
        elif self.toggle[10].state == 'down':
            self.result.text = couples(self.message.text)
        elif self.toggle[11].state == 'down':
            self.result.text = doubleCifir(args.id, self.message.text, self.key.text)
        elif self.toggle[12].state == 'down':
            self.result.text = fence(args.id, self.message.text)
        elif self.toggle[13].state == 'down':
            self.result.text = greatcipher(args.id, self.message.text)
        elif self.toggle[14].state == 'down':
            self.result.text = gronsfeld(args.id, self.message.text, self.key.text)
        elif self.toggle[15].state == 'down':
            self.result.text = hill2x2(args.id, self.message.text, self.key.text)
        elif self.toggle[16].state == 'down':
            self.result.text = hill3x3(args.id, self.message.text, self.key.text)
        elif self.toggle[17].state == 'down':
            self.result.text = homophonic(args.id, self.message.text)
        elif self.toggle[18].state == 'down':
            self.result.text = lattice(self.message.text)
        elif self.toggle[19].state == 'down':
            self.result.text = playfair(args.id, self.message.text)
        elif self.toggle[20].state == 'down':
            self.result.text = polibiy(args.id, self.message.text)
        elif self.toggle[21].state == 'down':
            self.result.text = ports(args.id, self.message.text)
        elif self.toggle[22].state == 'down':
            self.result.text = powVishener(args.id, self.message.text, self.key.text)
        elif self.toggle[23].state == 'down':
            self.result.text = psevdo(args.id, self.message.text)
        elif self.toggle[24].state == 'down':
            self.result.text = replace(args.id, self.message.text)
        elif self.toggle[25].state == 'down':
            self.result.text = rot13(self.message.text)
        elif self.toggle[26].state == 'down':
            self.result.text = rotors(args.id, self.message.text)
        elif self.toggle[27].state == 'down':
            self.result.text = rsa(args.id, self.message.text, self.key.text)
        elif self.toggle[28].state == 'down':
            self.result.text = syllables(args.id, self.message.text)
        elif self.toggle[29].state == 'down':
            self.result.text = tarabar(self.message.text)
        elif self.toggle[30].state == 'down':
            self.result.text = thritemius(args.id, self.message.text, self.key.text)
        elif self.toggle[31].state == 'down':
            self.result.text = typex(args.id, self.message.text)
        elif self.toggle[32].state == 'down':
            self.result.text = vernam(args.id, self.message.text, self.key.text)
        elif self.toggle[33].state == 'down':
            self.result.text = vishener(args.id, self.message.text, self.key.text)
        elif self.toggle[34].state == 'down':
            self.result.text = xor(self.message.text, self.key.text)

    def getInfo(self, args):
        info = {
            '0':\
"The key is not needed.\n\
Encrypt: A = 1, B = 2, C = 3, ... X = 24, Y = 25, Z = 26.\n\
Decrypt: 1 = A, 2 = B, 3 = C, ... 24 = X, 25 = Y, 26 = Z.", # A1Z26
            '1':"", # ADFGVX
            '2':\
"Cipher for encrypt files.\n\
Message = path/to/file\n\
Key = password.", # AES
            '3':\
"Possible Key[a]: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25.", # Affine
            '4':\
"The key is not needed.\n\
Encrypt/Decrypt: A = Z, B = X, C = Y, ... X = 24, C = B, Z = A.", # Atbash
            '5':"", # Bacon
            '6':"", # Book
            '7':"", # Caesar
            '8':"", # CaesarS
            '9':"", # Codes
            '10':"", # Couples
            '11':"", # Double Cifir
            '12':"", # Fence
            '13':"", # Greatcipher
            '14':"", # Gronsfeld
            '15':"", # Hill[2x2]
            '16':"", # Hill[3x3]
            '17':"", # Homophonic
            '18':"", # Lattice
            '19':"", # PlayFair
            '20':"", # Polibiy
            '21':"", # Ports
            '22':"", # PowVishener
            '23':"", # Psevdo
            '24':"", # Replace
            '25':"", # ROT13
            '26':"", # Rotors
            '27':"", # RSA
            '28':"", # Syllables
            '29':"", # Tarabar
            '30':"", # Thritemius
            '31':"", # Typex
            '32':"", # Vernam
            '33':"", # Vishener
            '34':"" # XOR
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

        self.key = TextInput(hint_text = "Key[s] for Cipher", size_hint = [1,.155])
        right.add_widget(self.key)

        self.message = TextInput(hint_text = "Encrypt/Decrypt the message")
        right.add_widget(self.message)

        self.result = TextInput(readonly = True, hint_text = "Result of Encryption/Decryption", background_color = [1,1,1,.8])
        right.add_widget(self.result)

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    CryptographyApp().run()
