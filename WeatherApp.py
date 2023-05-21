from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest
import requests
import json

API_Key = "42d68fe5356cf4ba70699c49eaba4a91"

def get_weather_data(city_name):
  """
  This function fetches weather data from OpenWeatherMap API for a given city name.

  Args:
    city_name: The name of the city to fetch weather data for.

  Returns:
    A dictionary containing the weather data for the given city.
  """

  # Get the API key from OpenWeatherMap website.
  api_key = API_Key

  # Create the URL for the API request.
  url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)

  # Make the API request.
  response = requests.get(url)

  # Check if the request was successful.
  if response.status_code == 200:
    # The request was successful, so we can parse the JSON response.
    data = json.loads(response.content)

    # Return the weather data.
    return data

  else:
    # The request was not successful, so we raise an exception.
    raise Exception("Error fetching weather data from OpenWeatherMap API.")



class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()

    def search_location(self):
        search_url = f"https://api.openweathermap.org/data/2.5/weather?q={self.search_input.text}&appid={API_Key}"
        request = UrlRequest(search_url, self.found_location)

    def found_location(self, request, data):
        self.search_results.update_weather_data(get_weather_data(self.search_input.text))


    class RV(RecycleView):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.data = [] 

        def update_weather_data(self, weather_data):
            self.data.append(weather_data)
            self.refresh_from_data()

class WeatherApp(App):
  def build(self):
    add_location_form = AddLocationForm()
    return add_location_form

if __name__ == "__main__":
  WeatherApp().run()
