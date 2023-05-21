from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import json


class WeatheryApp1(App):
    def build(self):
        root = BoxLayout()

        # Create a label to display the city name
        city_label = Label(text="City")

        # Create a text input to enter the city name
        city_input = TextInput()

        # Create a button to get the weather
        get_weather_button = Button(text="Get Weather")

        # Create a label to display the weather
        weather_label = Label()

        # Bind the text input to the weather label
        city_input.bind(text=weather_label.text)

        # Bind the get weather button to a function that gets the weather
        get_weather_button.bind(on_press=self.get_weather)

        # Add all the widgets to the root layout
        root.add_widget(city_label)
        root.add_widget(city_input)
        root.add_widget(get_weather_button)
        root.add_widget(weather_label)

        return root

    def get_weather(self, instance):
        # Get the city name from the text input
        city = city_input.text

        # Create a URL request to the OpenWeatherMap API
        weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=YOUR_API_KEY".format(city)

        # Make the request
        request = UrlRequest(weather_url)

        # Wait for the request to finish
        request.wait()

        # Get the response data
        data = json.loads(request.data)

        # Get the weather conditions
        conditions = data['weather'][0]['description']

        # Get the temperature
        temperature = data['main']['temp']

        # Set the text of the weather label
        weather_label.text = "{}: {}°C".format(conditions, temperature)


if __name__ == "__main__":
    WeatheryApp1().run()
