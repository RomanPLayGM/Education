a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - (4 * a * c)
if d >= 0:
    x1 = (((-1 * b) + (d ** 0.5)) / (a * 2))
    x2 = (((-1 * b) - (d ** 0.5)) / (a * 2))
    if x2 == x1:
        print(x1)
    else:
        if x1 > x2:
            print(x2, x1)
        else:
            print(x1, x2)
else:
    exit()
