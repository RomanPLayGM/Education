class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not (isinstance(self.a, int)) or not (isinstance(self.b, int)) or not (isinstance(self.c, int)) or (self.a <= 0 or self.b <= 0 or self.c <= 0):
            return 1
        elif not (self.a + self.b > self.c) or not (self.a + self.c > self.b) or not (self.b + self.c > self.a):
            return 2
        else:
            return 3


a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
