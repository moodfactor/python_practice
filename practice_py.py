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

class Structure:
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
import math

if __name__ == "__main__":
    class Stock(Structure):
        _fields = ["name", "shares", "price"]
    class Point(Structure):
        _fields = ["x", "y"]
    class Circle(Structure):
        _fields = ["radius"]
        def area(self):
            return math.pi * self.radius ** 2
        
    s = Stock("ACME", 50, 91.1)
    p = Point(2, 3)
    c = Circle(2)
    print(s.name, s.shares, s.price)
        
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    
    @abstractmethod
    def write(self, data):
        pass       

def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError("Expected an IStream")
    obj.serialize(stream)

import io 

IStream.register(io.IOBase)

class FileStream(IStream):
    def __init__(self, name):
        self.name = name
f = open('foo.txt', 'w')
print(isinstance(f, IStream))
f.close

# Base class. Uses a descriptor to set a value
class Descriptor:
    
    def __init__(self, name= None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Descriptor for enforcing types on attributes
class Typed(Descriptor):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        super().__set__(instance, value)
        
# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
      #  if value < 0:
        #    raise ValueError('Expected >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super().__init__(name, **opts)
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super().__set__(instance, value)

class Worker(Typed):
    expected_type = str

class UnsignedWorker(Worker, Unsigned):
    pass

class MaxSizedWorker(Worker, MaxSized):
    pass

class TypedWorker(Worker, Typed):
    expected_type = str

class Workerimp:
    name = MaxSizedWorker('name', size=20)
    age = UnsignedWorker('age')
    pay = TypedWorker('pay', expected_type=str)
    
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

s = Workerimp('Ahmed', '30', '5000')
print(s.name)
s.age = '5'
s.pay = '55000'
print(s.__dict__.items())

from collections.abc import Iterable
class A(Iterable):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
    def __iter__(self):
        return iter([self.a, self.b, self.c])

a = A()
print(a.__dict__)

import collections.abc
import bisect

class SortedItems(collections.abc.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial else []
        
    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)
        
items = SortedItems([5, 1, 3])
print(items.__dict__)
items.add(2)
print(items.__dict__)

import time

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod 
    def today(cls):
       t = time.localtime()
       return cls(t.tm_year, t.tm_mon, t.tm_mday)
   
a = Date(1989, 6, 10)
print(str(a))
a = Date.today()
print(a.__dict__)

class LoggedMappingMixin:
    
    __slots__ = ()
    
    def __getitem__(self, key):
        print('Getting ' + str(key))
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print('Setting {} = {!r}'.format(key, value))
        return super().__setitem__(key, value)
    
    def __delitem__(self, key):
        print('Deleting ' + str(key))
        return super().__delitem__(key)
    
class SetOnceMappingMixin:
    
    __slots__ = ()
    
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value)


class SetOnceDict(SetOnceMappingMixin, dict):
    pass

d = SetOnceDict()
d['x'] = 1
d['y'] = 2
print(d.__dict__)
print(d)
s = d['n'] = 3
print(s)

import math
import operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(self.x, self.y)

    def distance(self,x,y):
        return math.hypot(self.x - x , self.y - y)

p = Point(2, 3)
d = operator.methodcaller('distance', 0, 0)(p)
print(d)

class Node:
    pass

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
        
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        
class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

t1 = Sub(Number(2), Number(3))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(3))
t4 = Add(Number(1), t3)

class Nodevisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if not meth:
            meth = self.generic_visit
        return meth(node)
    
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

class Evaluator(Nodevisitor):
    def visit_Number(self, node):
        return node.value
    
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)
    
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
    
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)
    
    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)
    
    def visit_Negate(self, node):
        return -self.visit(node.operand)        
