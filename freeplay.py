from itertools import count
def get_weather_data(city_name):
  """
  This function fetches weather data from OpenWeatherMap API for a given city name.

  Args:
    city_name: The name of the city to fetch weather data for.

  Returns:
    A dictionary containing the weather data for the given city.
  """

  # Import the necessary libraries.

e= [x  for x in range(10) if x % 2 == 0]
f= list(filter(lambda x: x%2 ==0, range(10)))
print(f'list comperehension {e}')
print("Functional progrmming with filter method" , f)
gi= list(map(lambda x: x%2 ==0, range(10)))
print(gi)
print("="*90)
gen_exp= (x for x in range(10) if x % 2 == 0)
print(f'generator Expression {list(gen_exp)}')

x = "global "

# example of nonlocal, global, globals fun in python statement
def outer():
    x = "local"
    def inner():
        global x
        x = "nonlocal"
        print("inner:", globals()['x'])
    inner()
    print("outer:", x)
# outer()
print("*" * 90)
# example of nonlocal, global, globals fun in python statement
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", globals()['x'])
    inner()
    print("outer:", x)
outer()
print(x)

print("x" * 85)

fresh_fruit = {'apple': 10,'banana': 8,'lemon': 5,}
if (count:= fresh_fruit.get('lemon', 0)) > 4:
    print(count)
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
assert a[0:5] == a[:5]
assert a[-3:] == a[5:]
