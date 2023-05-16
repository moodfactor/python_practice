import requests

url = "https://gist.githubusercontent.com/moodfactor/1d41f2d58a5903088d59ac9f576b0b9d/raw/27105e5f200e6a40eb3895919cb17a4af392b186/fruits.json"

response = requests.get(url)

if response.status_code == 200:
    fruits = response.json()

    for fruit in fruits["fruits"]:
        print(fruit["name"], fruit["price"])

else:
    print("Error fetching fruits")