class Person:
    _x = [1, 2, 3]


    def __init__(self, x):
        self.x = x

    @property
    def talk(self):
        return self._x


a = Person(1)
print(Person.__dict__)
print(a.__dict__)