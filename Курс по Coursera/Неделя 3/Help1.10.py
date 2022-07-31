a = float(input())
b = float(input())
c = float(input())
if a == 0:
    if b != 0:
        print(1, -c / b)
        exit()
    if b == 0 and c == 0:
        print(3)
        exit()
    if b == 0 and c != 0:
        print(0)
        exit()
d = b ** 2 - (4 * a * c)
if d >= 0:
    x1 = (((-1 * b) + (d ** 0.5)) / (a * 2))
    x2 = (((-1 * b) - (d ** 0.5)) / (a * 2))
    if x2 == x1:
        print(1, x1)
    else:
        if x1 > x2:
            print(2, x2, x1)
        else:
            print(2, x1, x2)
else:
    print(0)
