import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader
from kivy.network.urlrequest import UrlRequest
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.properties import StringProperty




class RadioScreen(GridLayout):
    
    text_value = StringProperty()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sound_loader = SoundLoader()
        self.url_request = UrlRequest("http://3vh.liveradiu.com:8000/128kp.mp3", on_success=self.on_success, on_failure=self.on_failure)

        self.text_value = "Quran Kareem Radio"
        self.button_play = Button(text="Play")
        self.button_stop = Button(text="Stop")
        self.text_input = TextInput()

        self.grid_layout = GridLayout(cols=2)
        self.grid_layout.add_widget(self.button_play)
        self.grid_layout.add_widget(self.button_stop)
        self.grid_layout.add_widget(self.text_input)

        self.add_widget(self.grid_layout)

        self.button_play.bind(on_press=self.play_radio)
        self.button_stop.bind(on_press=self.stop_radio)
        self.text_input.bind(text=self.change_station)

    def change_station(self, instance, value):
        
        self.text_value = value
        self.load_audio_stream(value)
    
    def play_radio(self):
        self.sound_loader.play()

    def stop_radio(self):
        self.sound_loader.stop()

    def change_station(self, text):
        self.url_request = UrlRequest(text, on_success=self.on_success, on_failure=self.on_failure)

    def on_success(self, request):
        self.sound_loader.load(request.result)

    def on_failure(self, request):
        print("Request failed")

    def load_audio_stream(self, url):
        try:
            self.url_request = UrlRequest(url, on_success=self.on_success, on_failure=self.on_failure)
        except Exception as e:
            print(e)

    def show_progress_bar(self):
        progress_bar = ProgressBar()
        self.add_widget(progress_bar)

    def hide_progress_bar(self):
        self.remove_widget(progress_bar)


class RadioApp(App):
    def build(self):
        return  RadioScreen()


if __name__ == "__main__":
    RadioApp().run()
