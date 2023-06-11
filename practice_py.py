# import time

# def get_day_plan():

#     day_plan = {}

#     for day in ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]:

#         task = input("What is your task for {}? ".format(day)).lower()

#         if task == "":
#             continue

#         day_plan[day] = task

#     return day_plan

# def show_weekly_plan(day_plan):

#     print("Your weekly plan:")

#     for day, task in day_plan.items():

#         print("  * {}: {}".format(day.capitalize(), task))

# def edit_day_plan(day_plan):

#     valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

#     while True:

#         day = input("What day do you want to edit? (Mon, Tue, Wed, Thu, Fri, Sat, Sun) ").lower()

#         if day not in valid_days:
#             print("Invalid day. Please try again.")
#             continue

#         elif day in valid_days:
#             new_task = input("What is your new task for {}? ".format(day)).lower()
#             day_plan[day]+= f', {new_task}'
#             break

#         elif new_task == "":
#             break

#         day_plan[day] = new_task

#     return day_plan

# def main():

#     day_plan = get_day_plan()

#     while True:

#         show_weekly_plan(day_plan)

#         edit = input("Do you want to edit a day? (y/n) ").lower()

#         if edit == "y":
#             day_plan = edit_day_plan(day_plan)

#         if edit == "n":
#             break

#     print("Your final schedule:")

#     show_weekly_plan(day_plan)

# if __name__ == "__main__":

#     main()
    
def avg(first: int, *rest: int) -> int:
    return int((first + sum(rest)) / (1 + len(rest)))
print(avg(1, 2, 3, 4, 5))

print(avg.__annotations__)

import html
from sys import maxsize

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    element = f'<{name}{attrs}>{html.escape(value)}<{name}>'
    return element

print(make_element('item', 'Albatross', size='large', quantity=6))

def recv(maxsize, *, name, age):
    print(maxsize, name, age)

print(recv(1024, name='Bob', age=25))

_no_value = object()
def spam(a, b = _no_value):
    if not b :
        print('No b value supplied')
    print(a, b) 
spam(3,"d")

from functools import partial
s1 = partial(spam, 1)   

import requests

response = requests.get('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')

if response.status_code == 200:
    for line in response.content.decode('utf-8').splitlines():
        print(line)
else:
    print(response.status_code)
    print(response.content)

from urllib.request import urlopen

def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format(**kwargs))
    return opener


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

from queue import Queue
from functools import wraps


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key,value) for key, value in locals.items()
                            if callable(value) )
        # Redirect special methods
        def __len__(self):
            return self.__dict__['__len__']()

def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()

s = Stack()
print(s)

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self) -> str:
        return f'Pair({self.x}, {self.y})'
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'
    
p = Pair(3, 4)
print(p.__str__())

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}  

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

class MyContextManager:

    def __init__(self):
        print("Entering context")

    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")
        if exc_type is not None:
            print("Exception occurred:", exc_type, exc_value)

with MyContextManager() as cm:
    print("Inside context")
    
class Person:
   def __init__(self, first_name):
       self.first_name = first_name
   
   @property
   def first_name(self):
       return self._first_name
   
   @first_name.setter
   def first_name(self, value):
       if not isinstance(value, str):
           raise TypeError('Expected a string')
       self._first_name = value
    
   @first_name.deleter
   def first_name(self):
      raise AttributeError("Can't delete attribute")

class SubPerson(Person):

    @Person.first_name.getter
    def name(self):
        print("Getting name")
        return super().first_name
    
    
    
s = SubPerson("Ahmed")
print(s.name)
s.name = "Ali"
print(s.name)

class Integer:
    def __init__(self,name):
        self.name = name
        
    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value
        
    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
p = Point(2, 3)
print(p.x)
print(p.y)
p.x = 5
p.y = 6
    
print(p.__dict__.items())


    


class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def lazy_name(self):
        if not hasattr(self, "_name"):
            self._name = "mood"
        return self._name
    
p = Person("Ahmed")

p.lazy_name
print(p.lazy_name)

