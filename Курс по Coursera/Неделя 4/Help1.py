a1 = int(input())
b1 = int(input())
c1 = int(input())
d1 = int(input())


def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(min1, c)
    min3 = min(min2, d)
    return min3


print(min4(a1, b1, c1, d1))
