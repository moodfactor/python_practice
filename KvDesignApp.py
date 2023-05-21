from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout





class Controller(FloatLayout):
    label_wid  = ObjectProperty(None)
    info = StringProperty()
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        
    
    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'

class KvDesignApp(App):
    
    def build(self):
        return Controller(info='Hello world')
    
if __name__ == '__main__':
    KvDesignApp().run()