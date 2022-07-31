class Test:
    # _a = 10
    def __init__(self, val):
        self.a = val

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, val):
        self._a = val


    # @a.setter
    # def a(self, value):
        # self._a = value

    # @a.deleter
    # def a(self):
        # del self._a


x = Test(50)
print(x.a)
# x.a = 150
# print(x.a)
# del x.a
# print(x.a)


class DescrInt:
    def __set_name__(self, owner, name):
        # setattr(self, name[1:], "")
        self.x = name[1:]
        # print(self)
        # print(owner)
        # print(name)

    def __get__(self, instance, owner):
        return instance.__dict__[self.x]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Ошибка")
        instance.__dict__[self.x] = value


class Test1:
    _a = DescrInt()
    _b = DescrInt()

    def __init__(self, a, b):
        self._a = a
        self._b = b


x = Test1(1, 2)

