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
        return f'Person (id = {self.id} name = "{self.name}")'

danny = Person(1, 'danny')
print(danny) # same as print(danny.__str__())
suzi = Person(2, 'suzi')
print(suzi)