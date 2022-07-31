import math


def perimeter(x1, y1, x2, y2, x3, y3):
    x_1 = max(x1, x2) - min(x1, x2)
    y_1 = max(y1, y2) - min(y1, y2)
    a = math.sqrt(x_1 ** 2 + y_1 ** 2)
    x_2 = max(x2, x3) - min(x2, x3)
    y_2 = max(y2, y3) - min(y2, y3)
    b = math.sqrt(x_2 ** 2 + y_2 ** 2)
    x_3 = max(x1, x3) - min(x1, x3)
    y_3 = max(y1, y3) - min(y1, y3)
    c = math.sqrt(x_3 ** 2 + y_3 ** 2)
    return a + b + c


x4, y4 = float(input()), float(input())
x5, y5 = float(input()), float(input())
x6, y6 = float(input()), float(input())
print(perimeter(x4, y4, x5, y5, x6, y6))
