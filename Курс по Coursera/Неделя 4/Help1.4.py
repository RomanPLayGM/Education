def IsPointInSquare(x, y):
    x2 = abs(x) - 1
    y2 = abs(y) - 1
    t = x2 <= 0 and y2 <= 0
    return print("YES" * t, "NO" * (not t), sep="")


IsPointInSquare(0.5, 0.5)

