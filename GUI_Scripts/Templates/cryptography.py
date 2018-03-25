from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput

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

class CryptographyApp(App):
    def build(self):
        root = BoxLayout(orientation = "horizontal", padding = 5)

        left = ScrollView(size_hint = [.4,1])
        right = BoxLayout(orientation = "vertical")

        leftGrid = GridLayout(cols = 2, size_hint_y = None)
        leftGrid.bind(minimum_height = leftGrid.setter('height'))

        for index in range(len(ciphers)):
            leftGrid.add_widget(ToggleButton(id = str(index), text = ciphers[index], size_hint_y = None, height = 30, state = "normal"))
            leftGrid.add_widget(Button(id = str(index), text = "<- Info", size_hint_y = None, height = 30, size_hint = [.4,1]))

        left.add_widget(leftGrid)

        rigthGrid = GridLayout(cols = 2, size_hint = [1,.155])

        rigthGrid.add_widget(Button(text = "Encrypt"))
        rigthGrid.add_widget(Button(text = "Decrypt"))

        right.add_widget(rigthGrid)

        right.add_widget(TextInput(hint_text = "Key[s] for Cipher", size_hint = [1,.155]))

        right.add_widget(TextInput(hint_text = "Encrypt/Decrypt the message"))
        right.add_widget(TextInput(readonly = True, hint_text = "Result of Encryption/Decryption", background_color = [1,1,1,.8]))

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    CryptographyApp().run()
