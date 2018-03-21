from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput

from bs4 import BeautifulSoup
import requests, fake_useragent

class ParserApp(App):

    def kernel(self, connection = False):
        self.textResult.text = ""
        self.textInfo.text = ""
        if self.userAgentC.active:
            ua = fake_useragent.UserAgent() 
            header = {'User-Agent':str(ua.random)}
            self.textInfo.text += header['User-Agent']
        ipSite = 'http://icanhazip.com'
        if self.userAgentC.active:
            adress = requests.get(ipSite, headers = header)
        else:
            adress = requests.get(ipSite)
        self.textInfo.text += "\n:: IP your network: %s"%adress.text
        if self.torProxieC.active:
            self.textInfo.text += ":: Connecting to the Tor network\n"
            proxie = {
                'http': 'socks5h://127.0.0.1:9050', 
                'https': 'socks5h://127.0.0.1:9050'
            }
        try:
            if self.userAgentC.active and self.torProxieC.active:
                adress = requests.get(ipSite, proxies = proxie, headers = header)
                connection = True
            elif self.torProxieC.active:
                adress = requests.get(ipSite, proxies = proxie)
                connection = True   
        except:
            self.textInfo.text += ":: Stopping connect to the Tor network\n"
            if self.userAgentC.active:
                adress = requests.get(ipSite, headers = header)
            else:
                adress = requests.get(ipSite)
        if connection:
            self.textInfo.text += ":: Connected to the Tor network\n"
            self.textInfo.text += ":: IP Tor network: %s"%adress.text
        try:
            url = self.textSite.text
            if connection:
                if self.userAgentC.active and self.torProxieC.active:
                    page = requests.get(url, proxies = proxie, headers = header)
                elif self.torProxieC.active:
                    page = requests.get(url, proxies = proxie)
            else:
                if self.userAgentC.active:
                    page = requests.get(url, headers = header)
                else:
                    page = requests.get(url)
            self.soup = BeautifulSoup(page.text, "html.parser")
        except: return False
        else: return True

    def runParse(self, args):
        if ParserApp.kernel(self):
            if self.textTag.text:
                if self.textAttribute.text:
                    if self.textAttribute.text == "inside":
                        for tag in self.soup.findAll(self.textTag.text):
                            self.textResult.text += "%s\n"%tag.text
                    else:
                        for tag in self.soup.findAll(self.textTag.text):
                            try:
                                self.textResult.text += "%s\n"%tag[self.textAttribute.text]
                            except KeyError: pass
                else: 
                    for tag in self.soup.findAll(self.textTag.text):
                        self.textResult.text += "%s\n"%str(tag)
            else: 
                for tag in self.soup.findAll('html'):
                    self.textResult.text += "%s\n"%str(tag)
            self.textInfo.text += ":: Parse successfully runned."
        else:
            self.textInfo.text += ":: Invalid URL: '%s'.\n"%self.textSite.text     

    def saveParse(self, args):
        if ParserApp.kernel(self):
            if self.nameFile.text: 
                if self.textTag.text:
                    if self.textAttribute.text:
                        if self.textAttribute.text == "inside":
                            with open(self.nameFile.text,"w") as file:
                                for tag in self.soup.findAll(self.textTag.text):
                                    file.write("%s\n"%tag.text)
                        else:
                            with open(self.nameFile.text,"w") as file:
                                for tag in self.soup.findAll(self.textTag.text):
                                    file.write("%s\n"%tag[self.textAttribute.text])
                    else:
                        with open(self.nameFile.text,"w") as file:
                            for tag in self.soup.findAll(self.textTag.text):
                                file.write("%s\n"%str(tag))
                else: 
                    with open(self.nameFile.text,"w") as file:
                        for tag in self.soup.findAll('html'):
                            file.write(str(tag))
                self.textInfo.text += ":: File '%s' successfully saved."%self.nameFile.text
            else:
                self.textInfo.text += ":: File is not saved.\n"
        else:
            self.textInfo.text += ":: Invalid URL: '%s'.\n"%self.textSite.text

    def clear(self, args):
        self.textResult.text = ""
        self.textInfo.text = ""

    def build(self):
        root = BoxLayout(
            orientation = "horizontal",
            padding = 5)

        left = BoxLayout(orientation = "vertical")

        buttonRun = Button(
            text = "Run in the terminal",
            size_hint = [1,.07],
            on_press = self.runParse)
        left.add_widget(buttonRun)

        self.textSite = TextInput(
            text = "http://",
            foreground_color = [0,0,0,1],
            font_size = 17, size_hint = [1,.07], 
            background_color = [1,1,1,.7])
        left.add_widget(self.textSite)
        
        gridLeft = GridLayout(
            size_hint = [1,.07],
            cols = 2)

        self.nameFile = TextInput(
            text = "result.txt",
            font_size = 17)
        gridLeft.add_widget(self.nameFile)

        buttonSave = Button(
            text = "Save in the file",
            on_press = self.saveParse)
        gridLeft.add_widget(buttonSave)

        left.add_widget(gridLeft)

        self.textResult = TextInput()
        left.add_widget(self.textResult)

        right = BoxLayout(
            orientation = "vertical",
            size_hint = [.5,1])

        gridRight = GridLayout(
            size_hint = [1,.22],
            cols = 2)

        userAgentL = Label(
            font_size = 16,
            text = ": : User-agent : :")

        self.userAgentC = CheckBox(
            size_hint = [1,.33],
            active = True)

        gridRight.add_widget(userAgentL)
        gridRight.add_widget(self.userAgentC)

        torProxieL = Label(
            font_size = 16,
            text = ": : Tor-proxies : :")

        self.torProxieC = CheckBox(
            size_hint = [1,.33],
            active = True)

        gridRight.add_widget(torProxieL)
        gridRight.add_widget(self.torProxieC)

        self.textTag = TextInput(
            hint_text = "Tag",
            font_size = 17,
            text = "")

        self.textAttribute = TextInput(
            hint_text = "Attribute",
            font_size = 17,
            text = "")

        gridRight.add_widget(self.textTag)
        gridRight.add_widget(self.textAttribute)

        right.add_widget(gridRight)
        self.textInfo = TextInput(
            background_color = [1,1,1,.7])
        right.add_widget(self.textInfo)

        right.add_widget(Button(
            size_hint = [1,.055],
            text = "Clear",
            on_press = self.clear)
        )

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    ParserApp().run()
