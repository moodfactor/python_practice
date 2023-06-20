from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class NewsHome(BoxLayout):
    pass


class NewsApp(App):
    def build(self):
        return NewsHome()


if __name__ == '__main__':
    NewsApp().run()
