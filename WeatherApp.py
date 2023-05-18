from kivy.app import App
from kivy.uix.recycleview import RecycleView

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(values)} for values in ["Palo Alto, MX", "Palo Alto, US"]]

class WeatherApp(App):
    pass

if __name__ == '__main__':
     WeatherApp().run()
