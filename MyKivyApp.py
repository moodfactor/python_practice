from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class MyFirstWidget(BoxLayout):
    txt_inpt = ObjectProperty(None)
    def check_status(self, btn):
        print(f'button state is: {btn.state}')
        print(f'text input text is: {self.txt_inpt.text}')

class MykivyApp(App):
    def build(self):
        return MyFirstWidget() 
    
    
if __name__ == '__main__':
    MykivyApp().run()
