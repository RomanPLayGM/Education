def IsPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1 - abs(x)


x1, y1 = float(input()), float(input())
if IsPointInSquare(x1, y1):
    print("YES")
else:
    print("NO")
