from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.lang import Builder
   

class RootWidget(BoxLayout):
    pass

class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(8, 5, 50, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        with self.canvas:
            Line(points=( 0, 0, 100, 100))
            Color(1, 0, 0, .5, mode='rgba')
            Rectangle(pos=self.pos, size=self.size)
       
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class Try(App):
    def build(self):
        root = RootWidget()
        c = CustomLayout()
        c.add_widget(
            AsyncImage(
                source="https://img.freepik.com/free-photo/moon-light-shine-through-window-into-islamic-mosque-interior_1217-2597.jpg",
                size_hint=(1, 1),
                pos_hint={"center_x":  .5, "center_y": .5  }))
        root.add_widget(
            AsyncImage(
                source="https://img.freepik.com/free-photo/moon-light-shine-through-window-into-islamic-mosque-interior_1217-2597.jpg",
                size_hint=(1, 1),
                pos_hint={"center_x": .5, "center_y": .5}))
        root.add_widget(c)
        return root
                        


    
if __name__ == "__main__":
    Try().run()