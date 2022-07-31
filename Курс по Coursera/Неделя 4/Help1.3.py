def IsPointInSquare(x, y):
    x2 = abs(x) - 1
    y2 = abs(y) - 1
    return x2 <= 0 and y2 <= 0


x1, y1 = float(input()), float(input())
if IsPointInSquare(x1, y1):
    print("YES")
else:
    print("NO")
