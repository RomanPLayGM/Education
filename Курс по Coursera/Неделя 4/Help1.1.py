import math


def distance(x1, y1, x2, y2):
    x = max(x1, x2) - min(x1, x2)
    y = max(y1, y2) - min(y1, y2)
    return math.sqrt(x ** 2 + y ** 2)


x3, y3 = float(input()), float(input())
x4, y4 = float(input()), float(input())
print(distance(x3, y3, x4, y4))
