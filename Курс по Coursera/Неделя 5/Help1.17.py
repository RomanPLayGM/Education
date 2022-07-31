a, b = int(input()), int(input())
c, d = int(input()), int(input())
e = int(input())
k = 0
for x in range(0, 1001):
    if x != e:
        x1 = (a * x ** 3 + b * x ** 2 + c * x + d)
        if x1 / (x - e) == 0:
            k += 1
print(k)
