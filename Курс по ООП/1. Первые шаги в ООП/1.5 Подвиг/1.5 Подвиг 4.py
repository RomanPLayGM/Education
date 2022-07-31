from random import randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [(Line, Rect, Ellipse)[randint(1, 2)](randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)) for i in range(217)]
for i in elements:
    if isinstance(i, Line):
        i.sp = i.ep = 0, 0
