def IsPointInArea(x, y):
    a1 = y >= -x and y >= 2*x + 2  # Первое это ур-ие 1 прямой, а второе это 2 прямой
    r1 = (x + 1)**2 + (y - 1)**2
    b1 = y <= -x and y <= 2*x + 2
    return (a1 and r1 <= 2 ** 2) or (b1 and r1 >= 2 ** 2)


x1, y1 = float(input()), float(input())
if IsPointInArea(x1, y1):
    print("YES")
else:
    print("NO")
