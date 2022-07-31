p = float(input())
x = float(input())
y = float(input())
x1 = x + (y / 100)
p1 = (x1 * p) / 100
x2 = x1 + p1
print(int(x2 // 1), int((x2 % 1) * 100 + 0.009))
