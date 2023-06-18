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

e = Evaluator()
print(e.visit(t4))

from functools import total_ordering

class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width
        
@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()
        
    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)
    
    def add_room(self, room):
        self.rooms.append(room)
        
    def __str__(self):
        return '{}: {} square foot {}'.format(self.name,
                                               self.living_space_footage,
                                               self.style)
        
    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage
    
    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage
    
h1 = House('h1', 'modern')
h1.add_room(Room('bedroom', 10, 7))
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Office', 12, 15))

h2 = House('h2', 'classic')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Office', 12, 15))
h2.add_room(Room('Wine Cellar', 12, 6))
h2.add_room(Room('Bathroom', 8, 10))

print(h1)
print(h2)
print(h1 == h2)
print(h1 < h2)
print(h1.__dict__.items())

print("*"*85)

import time
from functools import wraps

def timethis(func):
     
     '''
     Decorator that reports the execution time.
     '''
     @wraps(func)
     def wrapper(*args, **kwargs):
         start = time.time()
         result = func(*args, **kwargs)
         end = time.time()
         print(func.__name__, end - start)
         return result
     return wrapper

@timethis
def countdown2(n):
    [n for n in range(n)]

@timethis
def countdown(n):
    while n > 0:
        n -= 1
        
@timethis
def countdown3(n):
    (n for n in range(n))

countdown3(100_000)
countdown(100_000)
countdown2(100_000)
orig_countdown = countdown2.__wrapped__(100_000)
print(orig_countdown)

from inspect import Signature, Parameter

# Make a signature for a fun(x, y = 42, *, z = None)
parms = [
    Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
    Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default = 42),
    Parameter('z', Parameter.KEYWORD_ONLY, default = None)]
sig = Signature(parms)
print(sig)

def fun(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)
    
def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)

class Structure:
    __signature__ = make_sig()
    
    def __init(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, valu in bound_values.arguments.items():
            setattr(self, name, valu)
    
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')
    
class Point(Structure):
    __signature__ = make_sig('x', 'y')

import inspect

print(inspect.signature(Stock))

class DocMeta(type):
    def __init__(self, name, bases, dict):
        for key, value in dict.items():
            if key.startswith('__'):
                continue
            if not hasattr(value, '__doc__'):
                continue
            if not getattr(value, '__doc__'):
                raise TypeError('Docstring required')
        
        type.__init__(self, name, bases, dict)

class Structure(metaclass = DocMeta):
    pass

class Foo(Structure):
 
    def testing(self):
        '''
            this is a test doc existing func
        '''
        pass

s = Foo()
print(s.testing())

class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(cls, clsname, bases, clsdict)
    
class Root(metaclass = MyMeta):
    pass

class A(Root):
    def foo(self):
        pass
    
class B(Root):
    def barit(self):
        pass

import json

s = '{"name": "ACME", "shares": 50, "price": 490.1}'



from collections import OrderedDict

data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d
    
# data = json.loads(s, object_hook=JSONObject)
print(str(data))

print(json.dumps(data, indent=4))

class Point:

    """
    A class representing a point in 2D space.

    Attributes:
        x (int): The x-coordinate of the point.
        y (int): The y-coordinate of the point.

    Methods:
        serialize_instance(obj): Serializes an instance of the `Point` class to a dictionary.
        unserialize_object(d): Unserializes a dictionary to an instance of the `Point` class.
    """

    def __init__(self, x, y):
        """
        Initializes a new `Point` instance.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def serialize_instance(obj):
        """
        Serializes an instance of the `Point` class to a dictionary.

        Args:
            obj (Point): The `Point` instance to serialize.

        Returns:
            dict: A dictionary representing the `Point` instance.
        """
        d = {'__classname__': type(obj).__name__}
        d.update(vars(obj))
        return d

    classes = {
        'Point': Point
    }

    def unserialize_object(d):
        """
        Unserializes a dictionary to an instance of the `Point` class.

        Args:
            d (dict): The dictionary to unserialize.

        Returns:
            Point: The `Point` instance represented by the dictionary.
        """
        clsname = d.pop('__classname__', None)
        if clsname:
            cls = Point.classes[clsname]
            obj = cls.__new__(cls)
            for key, value in d.items():
                setattr(obj, key, value)
                return obj
        else:
            return d
        

    def unserialize_object2(d):
        clsname = d.get('__classname__', None)
        if clsname and clsname in Point.classes:
            cls = Point.classes[clsname]
            obj = cls.__new__(cls)
            # Make instance without calling __init__
            for key, value in d.items():
                if key != '__classname__':
                    setattr(obj, key, value)
            return obj
        else:
            return d



p = Point(2, 3)
s = json.dumps(p, default=Point.serialize_instance)
print(s)
p2 = json.loads(s, object_hook=Point.unserialize_object2)
print(p2.__dict__)

stocks = [
('GOOG', 100, 490.1),
('AAPL', 50, 545.75),
('FB', 150, 7.45),
('HPQ', 75, 33.2),
]

import sqlite3
db = sqlite3.connect('database.db')
c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS portfolio (symbol TEXT, shares INTEGER, price REAL)')
db.commit()

c.executemany('insert into portfolio values (?, ? , ?)', stocks)

db.commit()

for row in db.execute('SELECT * FROM portfolio'):
    print(row)
    
min_price = 100.0
for row in db.execute('SELECT * FROM portfolio where price < ?', (min_price,)):
    print(row)
    
from urllib import request, parse

url = 'http://httpbin.org/get'

parms = {
    'name1': 'value1',
    'name2': 'value2'

}

querystring = parse.urlencode(parms)
print(querystring)

# u = request.urlopen(url+'?' + querystring)
# resp  = u.read().decode('utf-8')
# print(resp[2:80])
# print(resp)

import requests

url = 'http://httpbin.org/get'

parms = {
    'name': 'mood',
    'job' : 'programmer'
}

"""
# response = requests.post(url, data = parms)
# print(response.text)


# class EchoHandler(BaseRequestHandler):
    
    def handle(self):
        print('Got connection from ', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)

# if __name__ == '__main__':
    serv = TCPServer(('', 20000), EchoHandler)
    serv.serve_forever()

# from socket import socket, AF_INET, SOCK_STREAM

# s = socket(AF_INET, SOCK_STREAM)
# s.connect(('localhost', 20000))
# s.send(b'Hello, world')
# s.recv(8192)
# s.close() 
 
"""

""" from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer


class EchoHandler(StreamRequestHandler):
    
    def handle(self):
        #sleep for 1000
        time.sleep(1000)
        
        print('Got connection from ', self.client_address)
        # self.rfile is a file-like object for reading
        for line in self.rfile:
            # self.wfile is a file-like object for writing
            self.wfile.write(line)
            time.sleep(1000)

if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 20000), EchoHandler)
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever() """

""" import cgi

def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)

    def register(self, method, path, function):
        self.pathmap[method.lower(), path] = function
        
import time
_hello_resp = '''
<html>
    <head>
        <title>Hello {name}</title>
    </head>
    <body>
        <h1>Hello {name}!</h1>
    </body>
</html>

'''

def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')
    
_localtime_resp = '''\
        <?xml version="1.0"?>
        <time>
           <year>{t.tm_year}</year>
           <month>{t.tm_mon}</month>
           <day>{t.tm_mday}</day>
           <hour>{t.tm_hour}</hour>
           <minute>{t.tm_min}</minute>
           <second>{t.tm_sec}</second>
        </time>
        '''
def localtime2(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')

if __name__ == '__main__':
    import resty
    from wsgiref.simple_server import make_server

    # Create the dispatcher and register functions
    dispatcher =PathDispatcher()
    
    dispatcher.register('GET', '/hello', hello_world)
    dispatcher.register('GET', '/localtime', localtime2)

    # Launch a basic server
    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080...')
    httpd.serve_forever()


def hello_world2():
    return "Hello, world!"


def localtime():
    return time.asctime()

u = request.urlopen('http://localhost:8080/hello?name=Bob')
print(u.read().decode('utf-8')) """

""" class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplemented('must implement')

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False
    
    def handle_receive(self):
        'Perform the receive operation'
        raise NotImplemented('must implement')
    
    def wants_to_send(self):
        'Return True if sending is requested'
        return False
    
    def handle_send(self):
        'Perform the send operation'
        pass
    
import select

def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()
            time.sleep(1000)

import socket, time

class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)
        time.sleep(1000)
        
    def fileno(self):
        return self.sock.fileno()
    
    def wants_to_receive(self):
        return True
  
class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)

class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)
        
if __name__ == '__main__':
    handlers = [ UDPTimeServer(('', 14000)), UDPServer(('', 15000)) ]
    event_loop(handlers)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.sendto(b'', ('localhost', 14000))
 """
""" import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)
from threading import Thread

t = Thread(target=countdown, args=(10,), daemon=True)
t.start()
if t.is_alive():
    print('Still going...')
else: 
    print('Completed')
t.join()

class CountdownTask:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()

t.join() """

""" from threading import Thread, Event
import time

def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)
        
                                
started_evt = Event()
print('Launching countdown')
t = Thread(target= countdown, args=(10, started_evt))
t.setName = 'Countdown'

t.start()
started_evt.wait()
print('countdown is running')
print(t.__dict__)
t.join()

import threading

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
    
    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()
    
    def run(self):
        '''Run the timer and notify waiting threads after each interval.'''
        while True:
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
            time.sleep(self._interval)
    
    def wait_for_tick(self):
        '''Wait for the next tick of the timer.'''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(12)
ptimer.start()
 """
 
""" import threading

event = threading.Event()

def thread1f():
    event.wait()
    print('\n Thread 1')

def thread2f():
    print('\n Thread 2')
    event.set()


def thread3f():
    print('\n Thread 3')
    #event.clear()


thread1 = threading.Thread(target=thread1f)
thread2 = threading.Thread(target=thread2f)
thread3 = threading.Thread(target=thread3f)
thread1.start()
thread2.start()
thread3.start()

condition = threading.Condition()

queue = []
key = True

def producer():
    while key:
        item = produce_item()
        condition.acquire()
        queue.append(item)
        condition.notify()
        condition.release()

def consumer():
    while key:
        condition.acquire()
        while len(queue) == 0:
            condition.wait()
        
        item = queue.pop(0)
        condition.release()
        consume_item(item)

def produce_item():
    print('produce item')

def consume_item(item):
    print('consume item')
    global key
    key = False

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start() """

""" import threading
import time, random

# A list of items to be consumed by consumer threads
items = []

# A condition object to synchronize producer and consumer threads
condition = threading.Condition()

# A producer thread that generates items and notifies consumer threads
def producer():
    global items
    while True:
        with condition:
            # Generate a random item
            item = random.randint(0, 10)
            print(f"Producer: generated item {item}")
            # Append the item to the list
            items.append(item)
            # Notify one consumer thread that an item is available
            condition.notify()
        # Sleep for a random time
        time.sleep(random.random())

# A consumer thread that consumes items and waits for new items
def consumer():
    global items
    while True:
        with condition:
            # Wait for an item to be available
            condition.wait()
            # Pop the first item from the list
            item = items.pop(0)
            print(f"Consumer: consumed item {item}")
        # Sleep for a random time
        time.sleep(random.random())

# Create one producer thread and two consumer threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t3 = threading.Thread(target=consumer)

# Start the threads
t1.start()
t2.start()
t3.start() """

""" import threading
import time
import random

# A list of items to be consumed by consumer threads
items = []

# A condition object to synchronize producer and consumer threads
condition = threading.Condition()

# A boolean flag to indicate when to stop
stop = False

# A counter to keep track of the iterations
count = 0

# A producer thread that generates items and notifies consumer threads
def producer():
    global items, stop, count
    while not stop:
        with condition:
            # Generate a random item
            item = random.randint(0, 100)
            print(f"Producer: generated item {item}")
            # Append the item to the list
            items.append(item)
            # Notify one consumer thread that an item is available
            condition.notify()
            # Increment the counter
            count += 1
            # Check if the counter has reached 5
            if count == 5:
                # Set the stop flag to True
                stop = True
                # Notify all consumer threads to wake up
                condition.notify_all()
        # Sleep for a random time
        time.sleep(random.random())
    print("Producer: done")

# A consumer thread that consumes items and waits for new items
def consumer():
    global items, stop, count
    while not stop:
        with condition:
            # Wait for an item to be available
            condition.wait()
            # Check if the stop flag is True
            if stop:
                # Break out of the loop
                break
            # Pop the first item from the list
            item = items.pop(0)
            print(f"Consumer: consumed item {item}")
        # Sleep for a random time
        time.sleep(random.random())
    print("Consumer: done")

# Create one producer thread and two consumer threads
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t3 = threading.Thread(target=consumer)

# Start the threads
t1.start()
t2.start() """

import threading
import time
import random
import queue

# A queue of tasks to be done by worker threads
q = queue.Queue()

# A worker thread that consumes tasks from the queue
def worker():
    while True:
        # Get a task from the queue
        task = q.get()
        # Simulate some work
        print(f"Worker: doing task {task}")
        time.sleep(random.random())
        # Mark the task as done
        q.task_done()
        print(f"Worker: done task {task}")

# Create three worker threads
t1 = threading.Thread(target=worker, daemon=True)
t2 = threading.Thread(target=worker, daemon=True)
t3 = threading.Thread(target=worker, daemon=True)

# Start the worker threads
t1.start()
t2.start()
t3.start()

# Put some tasks in the queue
for i in range(10):
    q.put(i)

# Wait for all tasks to be done
q.join()

# Continue with the main thread
print("Main: all tasks are done")


        

