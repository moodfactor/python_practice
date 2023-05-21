from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty



class Marvel(BoxLayout):
    
    def hulk_smash(self):
        self.ids['hulk'] = "hulk: puny god!"
        self.ids["loki"].text = "loki: >_<!!!" # alternative syntax
        [print(k,v) for k,v in self.ids.items()]
        
class Kivy_propertiesApp(App):
    def build(self):
        return Marvel()
    
    
if __name__ == "__main__":
    Kivy_propertiesApp().run()