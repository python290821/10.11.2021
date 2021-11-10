import math
import random
class Person:
    def __init__(self, id=0, name='Incognito'):
        print('new person was created')
        self.id = id
        self.name = name

    def __str__(self):
        # this is default
        # return str(type(self)) + ' object at 0x0000027B2E009520'
        # return str(random.randint(50, 100))
        return f'Person (id: {self.id}, name: "{self.name}")'

danny = Person(1, 'danny')
print(danny) # same as print(danny.__str__())
suzi = Person(2, 'suzi')
print(suzi)

# targil:
# create 2 rectangles with width,
# height (3, 7) and (9, 12)
# print the 2 rectangles

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height

    def calc_hekef(self):
        return 2 * abs(self.width) + 2 * abs(self.height)

    def __str__(self):
        return f'Rectangle (width: {self.width}, height: {self.height}, '+\
               f'area: {self.calc_area()}, hekef: {self.calc_hekef()})'

rec1 = Rectangle(3.2, 7.88)
print(rec1)
print('area =',rec1.calc_area())
print('hekef =',rec1.calc_hekef())
rec2 = Rectangle(9, 12)
print(rec2)

class Myname:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __len__(self):
        return len(self.fname) + len(self.lname)

    def __str__(self):
        return f'Myname (fname: "{self.fname}", lname: "{self.lname}", '\
               f'len: {self.__len__()})';

danny = Myname('danny','cohen')
print(danny)
print('danny len = ', len(danny))
print('str = ',str(danny))

