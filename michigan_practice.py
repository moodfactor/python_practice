""" with open('practice.txt', 'r') as file:
    data = file.readlines()
    num_char = len(data)
    print(num_char)
    
f = open('first_forty', 'w')
with open('practice.txt', 'r') as s:
    for i in s:
        f.write(i) """

""" olympians = [('Laoise', 31, 'Paris'), ('Harry', 37, 'London'), ('Harald', 39, 'London'), ('Agatha', 49, 'Madrid')]

outfile = open("reduce_olympics.csv", "w")
header_row = "Name, age, City"
outfile.write(header_row)
print(header_row)
for name, age, city in olympians:
    row_string = f'{name}, {age}, {city}'
    outfile.write('\n' + row_string)
    print(row_string)

outfile.close() """

from typing import Any


class Limiter():
    __slots__ = ["age", "name", "job", '__dict__']

x = Limiter()
x.age = 40
print(x.age)
print(x.__dict__)
print(getattr(x, 'age'))    
setattr(x, 'name', 'ahmed')
print(x.name)

limiter = Limiter()
limiter.__dict__['age'] = 50
limiter.__dict__['name'] ='sara'
print(limiter.__dict__)

class Operators:
    def getage(self):
        return 34
    
    def setage(self, name, value: Any):
        self.name = value
    
    age = property(getage, setage, None, None)    


            
x = Operators()
Operators.age = 20 
print(x.age)

class AgeDesc(object):
    def __get__(self, instance, owner):
        return 36
    def __set__(self, instance, value):
        instance._age = value

class Descriptors(object):
    age = AgeDesc()
    
x = Descriptors()
print(x.age)