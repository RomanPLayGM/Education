class Mono1:
    def __init__(self):
        self.x = None


a = Mono1()
a.z = 10
# print(a.__dict__)
# print(Mono1.__dict__)


class Mono:
    _instance = None

    def __init__(self, z, d):
        if not Mono._instance:
            self._instance = Mono._instance
        self .instance()
        self.z = z
        self.d = d


    def instance(self):
        return Mono._instance

    # @classmethod
    # def up(cls):
    #     cls.My_Dict["x"] += 1


a = Mono(3, 5)
b = Mono(6, 10)
c = Mono(12, 15)
# a.up()
print(a.z)
print(b.z)
print(c.z)


class Test:
    _x = 10

    @property
    def x(self):
        return self._x


a = Test()
print(a.x)
