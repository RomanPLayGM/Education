def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


x1, y1 = float(input()), float(input())
x1_1, y1_1 = float(input()), float(input())
r1 = float(input())
if IsPointInCircle(x1, y1, x1_1, y1_1, r1):
    print("YES")
else:
    print("NO")
